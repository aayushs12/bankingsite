from django.db import models
class Reclog(models.Model):
    Recname=models.CharField(max_length=100)
    Recno=models.CharField(max_length=70)
    Amt=models.PositiveIntegerField()
    Curr=models.CharField(max_length=10)
