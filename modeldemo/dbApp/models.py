from django.db import models

# Create your models here.
class employee(models.Model):
    empNo=models.IntegerField()
    empName=models.CharField(max_length=20)
    empSalary=models.IntegerField()
    empAddress=models.CharField(max_length=50)

