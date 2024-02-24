from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    FirstName= models. CharField(max_length=100)
    LastName= models. CharField(max_length=100)
    Father_Name= models. CharField(max_length=100)
    
class Meta:
    db_table='datas'
