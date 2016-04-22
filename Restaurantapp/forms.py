from django import forms

from .models import *

class PostForm(forms.ModelForm):

        class Meta:
            model = Restaurant
            fields = ('name','price','telephone','street','city','zipCode','web','free',)

class PostForm_reserva(forms.ModelForm):

        class Meta:
            model = Restaurant
            fields = ('free',)

