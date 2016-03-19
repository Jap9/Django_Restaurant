from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

from .models import Restaurant
from .models import Client
from forms import PostForm


def mainpage(request):
    rests = Restaurant.objects.filter(name__isnull=False)
    return render(request, 'Restaurantapp/base.html', {'rests':rests})


def new_restaurant(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                #return redirect('Restaurantapp/base.html')
        else:
            form = PostForm()
        return render(request, 'Restaurantapp/new_restaurant.html', {'form': form})
