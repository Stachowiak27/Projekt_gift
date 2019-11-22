from django.contrib.auth.models import User
from django.db import models

# Create your models here.
TYPE = {
    (1,'fundacja'),
    (2,'organizacja pozarządowa'),
    (3,'zbiórka lokalna')
}

class Category(models.Model):
    name = models.CharField(max_length=64)

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=24, choices=TYPE)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=24)
    zip_code = models.PositiveIntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=True)