from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mac_adress = models.CharField(max_length=200)


    def __str__(self):
        return self.title


class YourModel:
    pass
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
