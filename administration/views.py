from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Designation


from teacher.models import Department, Designation
from .forms import *

def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'administration/login.html', context)

def admin_logout(request):
    logout(request)
    return redirect('login')

def add_designation(request):
    forms = AddDesignationForm()
    if request.method == 'POST':
        forms = AddDesignationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('designation')
    designation = Designation.objects.all()
    context = {'forms': forms, 'designation': designation}
    return render(request, 'administration/designation.html', context)

def admin_school(request):
    # Get the 'id' query parameter
    designation_id = request.GET.get('id')

    if designation_id:  # Ensure ID is provided
        forms = AddDesignationForm()
        if request.method == 'POST':
            forms = AddDesignationForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('designation')
        designation = Designation.objects.all()
        context = {'forms': forms, 'designation': designation}
        return render(request, 'administration/school.html', context)
    else:
        return HttpResponse("No ID provided.")
def admin_department(request):
    # Get the 'id' query parameter
    designation_id = request.GET.get('id')

    if designation_id:  # Ensure ID is provided
        forms = AddDesignationForm()
        if request.method == 'POST':
            forms = AddDesignationForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('designation')
        designation = Designation.objects.all()
        context = {'forms': forms, 'designation': designation}
        return render(request, 'administration/department.html', context)
    else:
        return HttpResponse("No ID provided.")
    
def detail(request, id):
    designation = get_object_or_404(Designation, id=id)
    return render(request, 'administration/detail.html', {'designation': designation})    
def detail(request, id):
    designation = get_object_or_404(Designation, id=id)
    return render(request, 'administration/designation_detail.html', {'designation': designation})

def designation_details(request):
    # Your view logic here
    return render(request, 'designation_detail.html')

# List View
def designation_list(request):
    designations = Designation.objects.all()  # Fetch all designations
    return render(request, 'designation_list.html', {'designations': designations})

# Detail View
def designation_detail(request, id):
    designation = get_object_or_404(Designation, id=id)
    return render(request, 'designation_detail.html', {'designation': designation})
     




  

def bangalore_bba(request):
    return render(request, 'administration/bangalorebba.html')

def bangalore_bms(request):
    return render(request, 'administration/bangalorebms.html')

def bangalore_mba(request):
    return render(request, 'administration/bangaloremba.html')

def kochi_bba(request):
    return render(request, 'administration/kochibba.html')

def kochi_mba(request):
    return render(request, 'administration/kochimba.html')
def facultyofmanagement(request):
    return render(request, 'administration/facultyofmanagement.html')
def engineering_and_technology(request):
    return render(request, 'administration/engineering_and_technology.html')





# List of departments
def department_list(request):
    departments = Department.objects.all()  # Fetch all department data
    return render(request, 'department.html', {'departments': departments})

# View for specific department details

