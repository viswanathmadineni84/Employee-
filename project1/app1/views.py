from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app1.models import Employee,LatestNews,AddCalender
from django.http import HttpResponse
from app1.forms import EmployeeForm,LatestNewsForm,AddCalenderForm
import csv

# Create your views here.
def homeview(request):
	return render(request, "app1/home.html")

@login_required
def hr_managerview(request):
	return render(request, "app1/hr_manager.html")

def Employeeview(request):
	return render(request, "app1/Employee.html")

def Add_Employeeview(request):
	data=EmployeeForm()
	if request.method=='POST':
		data=EmployeeForm(request.POST)
		if data.is_valid():
			data.save()
		return redirect('/viewemployeedata')
	return render(request, "app1/Add Employee.html",{'f':data})

def viewEmployeeDataview(request):
	data=Employee.objects.all()
	return render(request, "app1/viewemployeedata.html",{'g':data})

def UpdateView(request,id):
	data=Employee.objects.get(id=id)
	if request.method=='POST':
		data=EmployeeForm(request.POST,instance=data)
		if data.is_valid():
			data.save()
			return redirect('/viewemployeedata')
	return render(request,"app1/update.html",{'f':data})

def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Employeefile.csv"'
	data = Employee.objects.all()
	writer = csv.writer(response)
	writer.writerow(['Emp_Name','Emp_ID','Designation','Date_of_Joining','Department','Salary_Package','Experience'])
	for i in data:
		writer.writerow([i.Emp_Name,i.Emp_ID,i.Designation,i.Date_of_Joining,i.Department,i.Salary_Package,i.Experience])
	return response

def DeleteView(request,id):
	data=Employee.objects.get(id=id)
	data.delete()
	return redirect('/viewemployeedata')

def AddLatestNewsView(request):
	data=LatestNewsForm()
	if request.method=='POST':
		data=LatestNewsForm(request.POST)
		if data.is_valid():
			data.save()
			return redirect('/latestnews')
	return render(request, "app1/Add latest news.html",{'f':data})

def LatestNewsView(request):
	data=LatestNews.objects.all()
	return render(request,"app1/latestnews.html", {'h':data})

def AddCalenderView(request):
	data=AddCalenderForm()
	if request.method=='POST':
		data=AddCalenderForm(request.POST)
		if data.is_valid():
			data.save()
			return redirect('/calenderholidays')
	return render(request,"app1/AddCalender.html", {'f':data})

def CalenderholidaysView(request):
	data=AddCalender.objects.all()
	return render(request, "app1/calenderholidays.html", {'f':data})