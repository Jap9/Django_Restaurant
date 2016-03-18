from django.shortcuts import render
from django.utils import timezone

from .models import Restaurant
from .models import Client

# Create your views here.
from django.http import HttpResponse

#def mainpage(request):
#    return HttpResponse("hols")

def mainpage(request):
    rests = Restaurant.objects.filter(web="http://www.aaaa.com/")
    return render(request, 'Restaurantapp/base.html', {'rests':rests})