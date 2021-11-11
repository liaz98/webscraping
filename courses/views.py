from django.shortcuts import render
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer
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
