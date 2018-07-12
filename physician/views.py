from django.shortcuts import render
from django.http import HttpResponse
from .models import Physician

# Create your views here.
def doctors_list(request):
    doctors = Physician.objects.all()
    names = []
    for i in doctors:
        names.append(i.name)
    return HttpResponse(names)