import datetime
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Departments(models.Model):
    name = models.CharField(max_length=128)

class Workers(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

class InProductList(models.Model):
    name = models.CharField(max_length=512)
    cost = models.BigIntegerField()
    count = models.BigIntegerField()
    unit = models.CharField(max_length=64)
    document = models.CharField(max_length=256)
    date = models.DateField(default=datetime.date.today)
    picture = models.CharField(max_length=256)
    receiverperson = models.CharField(max_length=128)
    transmitterperson = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class OutProductList(models.Model):
    getproductperson = models.CharField(max_length=256)
    whoperson = models.CharField(max_length=256)
    cost = models.BigIntegerField()
    count = models.BigIntegerField()
    unit = models.CharField(max_length=64)
    document = models.CharField(max_length=256)
    date = models.DateField(default=datetime.date.today)
    picture = models.CharField(max_length=256)

class Documents(models.Model):
    docname = models.CharField(max_length=256)
    docurl = models.CharField(max_length=256)
    date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=256)

class Category(models.Model):
    name=models.CharField(max_length=128)
    url=models.CharField(max_length=20)
    def __str__(self):
        return self.name