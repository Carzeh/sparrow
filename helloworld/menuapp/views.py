# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from menuapp.models import Food, Drink
from django.http import Http404


# This view takes all food items from the database, and passes them as an object to the food.html template when it is rendered by the user's browser
def food(request):
	foods = Food.objects.all()
	if foods:
		return render(request,'templates/food.html',{'foods':foods}) 
	else:
		raise Http404	

# This view takes all drink items from the database, and passes them as an object to the drinks.html template when it is rendered by the user's browser
def drinks(request):
	drinks = Drink.objects.all()
	if drinks:
		return render(request,'templates/drinks.html',{'drinks':drinks})
	else:
		raise Http404	