from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=20)

class Book(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    fathername = models.CharField(max_length=100)


    def __str__(self):
        return self.name

