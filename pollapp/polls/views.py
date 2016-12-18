from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello,world.You're at the polls index.")

def detail(request,question_id):
	return HttpResponse("Hi,You are looking at question %s." % question_id)

def result(request,question_id):
	response = "You're looking at result of question %s ."
	return HttpResponse(response % question_id)

def vote(reuest,question_id):
	return HttpResponse("You're are voting on question %s." % question_id)

