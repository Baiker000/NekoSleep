from django.shortcuts import render
import datetime
from dateutil import parser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.models import Dream, User
from .serializers import DreamSerializer, UserSerializer
# Create your views here.

def validate_data_format(date_text):
    try:
        valid_data = parser.parse(date_text).strftime("%Y-%m-%d")
        return valid_data
    except:
        return None

class DreamViewSet(viewsets.ModelViewSet):

    #queryset = Dream.objects.filter(author=user)
    #queryset = Dream.objects.all().order_by('dream_date')
    serializer_class = DreamSerializer

    def perform_authentication(self, request):
        self.user = request.user

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Dream.objects.filter(author=self.user).order_by('dream_date').reverse()
        return queryset

    # def create(self, request, *args, **kwargs):
    #     print (request.data['dream_date'])
    #     super(DreamViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.user)



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def perform_authentication(self, request):
        self.user = request.user

    def get_queryset(self):
        queryset = User.objects.filter(id=self.user.id)
        return queryset