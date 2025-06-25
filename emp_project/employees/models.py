from django.db import models

# Create your models here.
class Department(models.Model):
    dname = models.CharField(max_length=50)
    d_location = models.CharField(max_length=50)

    def __str__(self):
        return self.dname
    

class Employee(models.Model):
    ename = models.CharField(max_length=60)
    age = models.IntegerField()
    salary = models.FloatField()
    email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
class EmployeeProfile(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)
    bio=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images',null=True,blank=True)
    resume=models.ImageField(upload_to='resume',null=True,blank=True)
    linkedin=models.URLField(null=True,blank=True)
    phone_no=models.CharField(max_length=15)
    def __str__(self):
        return self.employee.ename