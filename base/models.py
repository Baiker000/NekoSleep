from django.db import models
import django.contrib.auth.models as auth
from django.conf import settings
import io
import os
import uuid
import base64
from datetime import date as dt
from django.utils.timezone import now
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from .storage import OverwriteStorage
from django.core.exceptions import ValidationError
from polymorphic.models import PolymorphicModel
from .validators import validate_file_extension

# Create your models here.
def user_dir_path(instance, filename):
    if instance.id:
        return 'user_{0}/avatar'.format(instance.id)
    else:
        return None

def user_dir_patch_audio_text(instance, filename):
    return 'user_{0}/dream_{1}/audio_text.ogg'.format(instance.author.id, instance.id)
# FIXME
def make_square(im, min_size=300, fill_color=(255, 255, 255, 255)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
 #   new_im.paste(im, ((size - x) / 2, (size - y) / 2))
    return new_im

def generate_uuid():
    return uuid.uuid4()

class Dream(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=256)
    text = models.TextField()
    audio_text = models.FileField(upload_to=user_dir_patch_audio_text, blank=True, null=True, validators=[validate_file_extension])
    tags = models.ManyToManyField('Tag', blank=True)
    # map =
    # series = models.ForeignKey('self', blank= True, null=True, on_delete=models.SET_NULL)  # uses if we continue previous dream
    dream_date = models.DateField(blank=True, null=True, default=None)
    need_pas = models.BooleanField(default=False)
    pas = models.CharField(blank=True, max_length=8, default='')
    # related_files = models.FileField()

    # def get_series(self):
    #     current = self
    #     ret = []
    #     while current.series:
    #         ret.append(current.series)
    #         current = current.series
    #     return ret

    def __str__(self):
        if self.title:
            return self.title
        else:
            return ' '.join(self.text.split()[:5])

    # def clean(self, *args, **kwargs):
    #     if self.series:
    #         if self.series.author != self.author:
    #             raise ValidationError('Author not match')
    #         if self.series.series == self:
    #             raise ValidationError('Loop series')
    #     super(Dream, self).clean(*args, **kwargs)

    # Add this method to your model
    # def audio_file_player(self):
    #     """audio player tag for admin"""
    #     if self.audio_text:
    #         file_url = settings.MEDIA_URL + str(self.audio_text)
    #         player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (
    #             file_url)
    #         return player_string
    #
    # audio_file_player.allow_tags = True
    # audio_file_player.short_description = ('Audio file player')


# Tag
# it must be abstract, but i need relations to all tag
# don't add to tag
class Tag(PolymorphicModel):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class CommonTag(Tag):
    pass


class UserTag(Tag):
    author = models.ManyToManyField('User')


class ShadowTag(Tag):
    author_vote = models.ManyToManyField('User')

# Tag end

class Map(models.Model):
    pass



class User(auth.AbstractUser):
    # for protection sake
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    avatar = models.ImageField(upload_to=user_dir_path, default='user_None/avatar', storage=OverwriteStorage())

    def save(self, *args, **kwargs):
        if self.avatar and self.avatar != 'user_None/avatar':
            img = Image.open(io.BytesIO(self.avatar.read()))
            output = io.BytesIO()
            img = make_square(img)
            img.save(output, format='PNG')
            output.seek(0)
            self.avatar = InMemoryUploadedFile(output, 'ImageField', "%s.png" %self.avatar.name.split('.')[0] , 'image/png', output.getbuffer().nbytes, None)
        else:
            self.avatar = 'user_None/avatar'
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username