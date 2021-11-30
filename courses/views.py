from django.shortcuts import render
from .models import Course, Category, News
from .serializers import CourseSerializer, CategorySerializer, NewsSerializer
from rest_framework import generics

# Create your views here.

# class CategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.filter(parent__isnull=True)
#     serializer_class = CategorySerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class NewsListView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
