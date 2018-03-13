from django.db import models
from mainproject.settings import BASE_DIR

# Create your models here.


def directory(instance, file):
    return '{0}/static/{1}'.format(BASE_DIR, file)

class Project(models.Model):
    idn=models.CharField(max_length=100,primary_key=True,default=' ')
    name=models.CharField(max_length=100,default=' ')
    keyword=models.CharField(max_length=200,default=' ')
    photo = models.ImageField(upload_to=directory)
    url=models.URLField(default='/')
    score=models.FloatField(max_length=100,null=True)
