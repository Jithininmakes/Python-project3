
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import table


def sound (request):
   x=table.objects.all()

   return render(request,"index.html", {'y':x})

