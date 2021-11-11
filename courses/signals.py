from django.db.models.signals import post_save
from course_sites.coursera import getTitle, getDescription, getRating, getEnrolled, getOfferedBy
from course_sites.udemy import getTitleUdemy, getRatingUdemy, getEnrolledUdemy, getOfferedByUdemy, getDescriptionUdemy
from .models import Course, CourseUrl
from django.dispatch import receiver
import requests
from bs4 import BeautifulSoup

@receiver(post_save, sender=CourseUrl)
def create_courseurl(sender, instance, created, **kwargs):
    req = requests.get(str(instance))
    soup: BeautifulSoup = BeautifulSoup(req.text, features="lxml")
    if created:
        print(instance.url[0:21])
        if str(instance.url[0:24]) == "https://www.coursera.org":
            print(instance)
            Course.objects.create(
                url = instance,
                title=getTitle(soup),
                description=getDescription(soup),
                rating=getRating(soup),
                enrolled=getEnrolled(soup),
                offered=getOfferedBy(soup),
                course_type=Course.COURSERA
            )
        elif str(instance.url[0:21]) == "https://www.udemy.com":
            print(len(instance.url))
            Course.objects.create(
                url=instance,
                title=getTitleUdemy(soup),
                description=getDescriptionUdemy(soup),
                rating=getRatingUdemy(soup),
                enrolled=getEnrolledUdemy(soup),
                offered=getOfferedByUdemy(soup),
                course_type=Course.UDEMY
            )
        print('Course created')


@receiver(post_save, sender=CourseUrl)
def save_courseurl(sender, instance, created, **kwargs):
    if created:
        print('buyam ishladi')
        instance.save()