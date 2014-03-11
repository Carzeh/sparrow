from django.contrib import admin
from menuapp.models import MenuItem,Drink,Food

class FoodAdmin(admin.ModelAdmin):
	list_display = ['name','french_name','price']
	list_filter = ['is_brunch','is_dinner']

class DrinkAdmin(admin.ModelAdmin):
	list_display = ['name','french_name','price']
	list_filter = ['is_soft','is_hard']

admin.site.register(Drink, DrinkAdmin)
admin.site.register(Food, FoodAdmin)