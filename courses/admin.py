from django.contrib import admin
from .models import Course, CourseUrl, Category, News
from mptt.admin import MPTTModelAdmin

admin.site.site_header = 'Admin Dashboard'

class CourseUrlAdmin(admin.ModelAdmin):
    ordering = ['url']
    fields = ['url', 'category']
    list_display = ['url', 'category']
    list_filter = ['url']
    search_fields = ['url']

class CourseAdmin(admin.ModelAdmin):
    ordering = ['title']
    fields = ['url', 'title', 'description', 'rating', 'enrolled', 'offered', 'course_type']
    list_display = ['url', 'title']
    list_filter = ['title', 'url']
    search_fields = ['title', 'url', 'course_type']






admin.site.register(Category, MPTTModelAdmin)
admin.site.register(CourseUrl, CourseUrlAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(News)