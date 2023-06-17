from django.shortcuts import render
from django.http import HttpResponse
from school.models import Pupil
# Create your views here.

def get_pupils(request):
    pupils=Pupil.objects.all()
    context={
        'pupils':pupils
    }
    return render(request,"pupils.html",context)