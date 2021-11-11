# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

soup : BeautifulSoup

def getTitle(soup):
    try:
        course_title = soup.find('div', class_='BannerS12n').find('h1').text
        return course_title
    except:
         course_title = soup.find('div', id='main').find('h1').text
         return course_title

def getDescription(soup):
    try:
        course_description = soup.find('div', class_='AboutS12n').find('div', class_='description').text.replace('Â', '').replace('â', "'")
        return course_description
    except:
        course_description = soup.find('div', class_='content').find('div', class_='content-inner').text.replace('Â', '').replace('â', "'")
        return course_description


def getRating(soup):
    try:
        course_rating = soup.find('div', class_='BannerS12n').find('span', class_='_16ni8zai m-b-0 rating-text number-rating number-rating-expertise').text.replace('stars', '')
        return course_rating
    except:
        course_rating = soup.find('div', class_='_1srkxe1s XDPRating').find('span', class_='_16ni8zai m-b-0 rating-text number-rating number-rating-expertise').text.replace('stars', '')
        return course_rating

def getEnrolled(soup):
    try:
        course_enrolled = soup.find('div', class_='BannerS12n').find('div', class_='_1fpiay2').find('strong').text
        return course_enrolled
    except:
        course_enrolled = soup.find('div', class_='rc-ProductMetrics').find('div', class_='_1fpiay2').find('strong').text
        return course_enrolled

def getOfferedBy(soup):

    try:
        course_offered=soup.find('div', class_='BannerS12n').find('div', class_='m-b-1s m-r-1').find('img')['title']
    except:
        course_offered=soup.find('div', class_='_1m6egy8n').find('div', class_='p-b-1s p-r-1').find('img')['title']
    return course_offered



# def coursera(url):
#     req = requests.get(url)
#     soup: BeautifulSoup = BeautifulSoup(req.text, features="lxml")
    # course = Course.objects.create(
    #        title=getTitle(soup),
    #        description=getDescription(soup),
    #        rating=getRating(soup),
    #        enrolled=getEnrolled(soup),
    #        offered=getOfferedBy(soup),
    #    )
    # return course

# coursera('https://www.coursera.org/specializations/learn-spanish')




