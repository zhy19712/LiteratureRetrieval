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


class Article(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=255, null=True)
    text = models.TextField(null=True)


class KeywordTitle(models.Model):
    keyword = models.CharField(max_length=255, null=True)


class KeywordText(models.Model):
    keyword = models.CharField(max_length=255, null=True)


class ScrapedUrls(models.Model):
    url = models.CharField(max_length=255, null=True)
