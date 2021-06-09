from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the person index.")


def patient(request):
    return

def admin(request):
    return