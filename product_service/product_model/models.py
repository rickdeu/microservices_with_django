from __future__ import unicode_literals
from django.db import models

# This is our model for user product details
class ProductDetails(models.Model):
    ### The following are the fields of our table
    product_id = models.CharField(max_length=10)
    product_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)

    ### It willl help to print the values
    def __str__(self):
        return f"{self.product_id} {self.product_category} {self.product_name} {self.availability} {self.price}"
    