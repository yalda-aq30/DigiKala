from django.shortcuts import render
from django.http import HttpResponse
def home_response(request):
    return HttpResponse("به وبسایت ما خوش آمدید")


def home_view(request):
    return render(request, 'home/home.html')


def base_view(request):
    return render(request, 'base.html')