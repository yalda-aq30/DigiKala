from django.shortcuts import render
from django.http import HttpResponse
def home_response(request):
    return HttpResponse("به وبسایت ما خوش آمدید")
