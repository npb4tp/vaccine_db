from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment

def index(request):
    return render(request, 'landing.html')

def patient(request):
    appoint_list = Appointment.objects.all()
    return render(request, 'patient.html', {'appoint_list': appoint_list})
