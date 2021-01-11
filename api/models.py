from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField("键", max_length=200, db_index=True)
    value = models.SlugField("值", max_length=200, db_index=True)