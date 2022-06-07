# Import necessary classes
from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Course, Student, Order


# Create your views here.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    course_list = Course.objects.all().order_by('-price')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of topics: ' + '</p>'
    response.write(heading1)

    for topic in top_list:
        para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
        response.write(para)

    for course in course_list:
        if course.for_everyone:
            para = '<p>' + str(course.id) + ': ' + str(course) + 'This course is for everyone' + '</p>'
        else:
            para = '<p>' + str(course.id) + ': ' + str(course) + 'This course is not for everyone' + '</p>'
        response.write(para)
    return response

def about(request):
    response = HttpResponse()
    heading1 = '<p>' + 'About the page ' + '</p>'
    response.write(heading1)
    para = '<p>' + 'This is an E-learning Website! Search our Topics to find all available Courses.' + '</p>'
    response.write(para)
    return response

def detail(request, top_no):
    response = HttpResponse()
    heading1 = '<p>' + 'details of the topic ' + '</p>'
    response.write(heading1)
    topic = Topic.objects.get(id=top_no)
    top_name = topic.name
    para = f"<p>Topic name {top_name} and category {topic.category}</p>"
    response.write(para)
    course_list = Course.objects.filter(topic__name=top_name)
    para = "<p>List of Courses</p>"
    response.write(para)
    for course in course_list:
        para = "<p>" + str(course.name) + '</p>'
        response.write(para)
