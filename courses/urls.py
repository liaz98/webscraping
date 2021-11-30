from django.urls import path
from .views import CourseList, CourseDetail, CategoryView, CategoryDetailView, NewsListView, NewsDetailView

urlpatterns = [
    path('news/', NewsListView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view() ),
    path('courses/', CourseList.as_view()),
    path('course/<int:pk>/', CourseDetail.as_view())
]