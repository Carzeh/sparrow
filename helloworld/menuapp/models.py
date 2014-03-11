from django.db import models

# Create general menu item class
class MenuItem(models.Model):

	name = models.CharField(max_length=150)
	french_name = models.CharField(max_length=150)
	description = models.CharField(max_length=150,null=True,blank=True)
	french_description = models.CharField(max_length=150,null=True,blank=True)
	price = models.DecimalField(max_digits=4,decimal_places=2,blank=True,null=True)

	# second price allows for food or drink that has two prices, e.g. coffee $2.50, coffee with milk $3.00
	second_price = models.DecimalField(max_digits=4,decimal_places=2,blank=True,null=True)

	def __unicode__(self):
		return self.name

# Drink has two extra options and inherits general menu class
class Drink(MenuItem):

	is_soft = models.BooleanField()
	is_hard = models.BooleanField()

# Food has three extra options and inherits general menu class
class Food(MenuItem):

	is_dinner = models.BooleanField()
	is_brunch = models.BooleanField()
	is_side = models.BooleanField()



