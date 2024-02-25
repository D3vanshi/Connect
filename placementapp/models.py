from django.db import models

# Create your models here.
class add_data(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    mail=models.EmailField()
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    password=models.CharField(max_length=20)



