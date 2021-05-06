from django.shortcuts import render
from . import models
from rest_framework import generics
from . import serializers
from rest_framework import viewsets
# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset =models.Lead.objects.all()
    serializer_class = serializers.reactAppSrializer

# class AlarmView(viewsets.ModelViewSet):
#     queryset = models.Alarm.objects.all()
#     serializer_class = serializers.AlarmSrializer

class DeptView(viewsets.ModelViewSet):
    queryset = models.Dept.objects.all()
    serializer_class = serializers.DeptSrializer

# class CategoryListView(viewsets.ModelViewSet):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerializer


# class TrackView(generics.ListCreateAPIView):
#     queryset = models.Track.objects.all().select_related('album')
#     serializer_class = serializers.TrackSerializer

from django.contrib.auth.models import User

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# class AuthorViewSet(generics.ListCreateAPIView):
#     """
#     List all workers, or create a new worker.
#     """
#     queryset = models.Author.objects.all()
#     serializer_class = serializers.AuthorSerializer

# from rest_framework import filters
# class BookViewSet(generics.ListCreateAPIView):
#     """
#     List all workkers, or create a new worker.
#     """
#     queryset = models.Book.objects.all()
#     serializer_class = serializers.BookSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['release_date']