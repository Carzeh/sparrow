from django.conf.urls import patterns,url
from menuapp import views


# If user goes to /drinks start the drinks view, if user goes to /food start the food view

urlpatterns = patterns('',
	url(r'^drinks/$',views.drinks,name='drinks'),
	url(r'^food/$',views.food,name='food'),
	url(r'^manger/$',views.food,name='food'),
	url(r'^boire/$',views.drinks,name='drinks'),

	)