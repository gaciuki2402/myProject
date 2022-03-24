from inspect import classify_class_attrs
from tkinter import CASCADE
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),

    )
    name=models.CharField(max_length=200)
    shirt_size=models.CharField(max_length=1, choices=SHIRT_SIZES)

class Runner(models.Model):
    Medal_Type=models.TextChoices("Medal_Type", "Gold, Silver,Bronze")
    name=models.CharField(max_length=200)
    medal=models.CharField(blank=True, choices=Medal_Type.choices, max_length=10)


class Library_Books(models.Model):
    Books=(
        ('C', 'Chemistry'),
        ('G', 'Geography'),
        ('M', 'Mathematics'),
        ('E', 'English'),
    )
    name=models.CharField(max_length=200)
    book=models.CharField(max_length=1, choices=Books)

class Fruit(models.Model):
    name=models.CharField(max_length=100, primary_key=True)

class Manufacturer(models.Model):
    pass
class car(models.Model):
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


# Create your models here.
