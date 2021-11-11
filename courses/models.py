from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, db_index = True)

    class MPTTMeta:
        unique_together = ('parent',)
        verbose_name_plural = 'categories'
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])



class CourseUrl(models.Model):
    url = models.CharField(primary_key= True, max_length=250)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='courseurl')
    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)


class Course(models.Model):
    UDEMY = 'Udemy'
    COURSERA = 'Coursera'
    COURSE_CHOICES = [
        (UDEMY, 'Udemy'),
        (COURSERA, 'Coursera'),
    ]

    url = models.OneToOneField(CourseUrl, on_delete=models.CASCADE, related_name='course')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    rating = models.FloatField(blank=True, null=True)
    enrolled = models.CharField(max_length=20, blank=True, null=True)
    offered = models.CharField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=10, choices=COURSE_CHOICES, default=UDEMY)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return str(self.url)





