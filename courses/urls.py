from django.urls import path
from .views import CourseList, CourseDetail, CategoryView, CategoryDetailView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view() ),
    path('courses/', CourseList.as_view()),
    path('course/<int:pk>/', CourseDetail.as_view())
]