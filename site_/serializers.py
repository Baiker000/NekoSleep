from rest_framework import serializers
from dateutil import parser
from base.models import Dream, Tag, CommonTag, UserTag, ShadowTag, User

def validate_data_format(date_text):
    try:
        valid_data = parser.parse(date_text).strftime("%Y-%m-%d")
        return valid_data
    except:
        return None


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')
        extra_kwargs = {
            'username': {'read_only': True},
            'email': {'read_only': True},
            'avatar': {'read_only': True}
        }


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name', 'description')


class DreamSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Dream
        fields = ('id', 'title', 'author', 'audio_text', 'tags', 'dream_date', 'text')
        extra_kwargs = {
            'author': {'read_only': True},
            'id': {'read_only': True}
        }

    def to_internal_value(self, data):
        data['dream_date'] = validate_data_format(data['dream_date'])

        return super(DreamSerializer, self).to_internal_value(data)

    # def to_representation(self, instance):
    #     representation = super(DreamSerializer, self).to_representation(instance)
    #     print (instance.dream_date)
    #     representation['dream_date'] = validate_data_format(instance.dream_date)
    #     return representation