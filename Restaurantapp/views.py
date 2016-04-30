from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.shortcuts import redirect

from .models import Restaurant
from forms import *


def mainpage(request):
    rests = Restaurant.objects.order_by('price')
    return render(request, 'Restaurantapp/base.html', {'rests': rests})


def new_restaurant(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = PostForm()
    return render(request, 'Restaurantapp/new_restaurant.html', {'form': form})


def delete_restaurant(request,rest_pk):
    delRest= Restaurant.objects.get(pk=rest_pk)
    delRest.delete()
    return redirect('http://127.0.0.1:8000/')


def reservar_restaurant(request):
    if request.method == "POST":
        form = PostForm_reserva(request.POST)
        if form.is_valid():

            return redirect('http://127.0.0.1:8000/')
    else:
        form = PostForm_reserva()
    return render(request, 'Restaurantapp/reservar_restaurant.html', {'form': form})
