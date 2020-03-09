from django.db import models

# Create your models here.


class ClientTest(models.Model):
    name = models.CharField("名称", max_length=100, default='')
    score = models.IntegerField("分数")
