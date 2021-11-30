# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
soup : BeautifulSoup

def getTitleUdemy(soup):
    course_title = soup.find('div', class_='clp-component-render').find('script').get_text().strip()
    course_json = json.loads(course_title)
    return course_json[0]['name']

def getDescriptionUdemy(soup):
    course_description = soup.find('div', class_='clp-component-render').find('script').get_text().strip()
    course_json = json.loads(course_description)
    return course_json[0]['description']


def getRatingUdemy(soup):
    course_rating = soup.find('div', class_='clp-component-render').find('script').get_text().strip()
    course_json = json.loads(course_rating)
    return course_json[0]['aggregateRating']['ratingValue']

def getEnrolledUdemy(soup):
    course_enrolled = soup.find('div', class_='clp-lead__element-item clp-lead__element-item--row').find("div", {"data-purpose":"enrollment"})
    course_enrolled = course_enrolled.text.strip().replace('students', '').strip()
    return course_enrolled

def getOfferedByUdemy(soup):
    course_offered = soup.find('div', class_='clp-component-render').find('script').get_text().strip()
    course_json = json.loads(course_offered)
    return course_json[0]['creator'][0]['name']








