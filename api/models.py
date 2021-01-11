from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField("键", max_length=200, db_index=True)
    value = models.SlugField("值", max_length=200, db_index=True)


class Proxy(models.Model):
    ip = models.CharField(max_length=50)
    port = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    protocal = models.CharField(max_length=50)
    position = models.CharField(max_length=50)