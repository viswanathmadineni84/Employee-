from django.db import models

# Create your models here.
class Employee(models.Model):
	Emp_Name=models.CharField(max_length=40)
	Emp_ID=models.IntegerField()
	Designation=models.CharField(max_length=130)
	Date_of_Joining=models.CharField(max_length=130)
	Department=models.CharField(max_length=130)
	Salary_Package=models.IntegerField()
	Experience=models.CharField(max_length=130)

class LatestNews(models.Model):
	OCCATION=models.CharField(max_length=200)

class AddCalender(models.Model):
	Date=models.CharField(max_length=50)
	Occation=models.CharField(max_length=200)