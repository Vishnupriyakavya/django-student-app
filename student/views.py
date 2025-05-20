from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import student
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'student/index.html')

def home(request):
    students=student.objects.all()
    context={
        'students': students
    }
    return render(request,'student/home.html',context)


def add_student(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        dept=request.POST['dept']
        student.objects.create(name=name,age=age,email=email,dept=dept)
        
        return redirect('home')
    return render(request,'student/add_student.html')




def delete_student(request, name):
    student_to_delete = student.objects.get(name=name)  # name=name left name as it is name field right name is the name we are passing
    student_to_delete.delete()
    return redirect('home')




def update_student(request, id):
    student_obj = get_object_or_404(student, id=id)

    if request.method == 'POST':
        student_obj.name = request.POST.get('name')
        student_obj.age = request.POST.get('age')
        student_obj.email = request.POST.get('email')
        student_obj.dept = request.POST.get('dept')
        student_obj.save()
        return redirect('home')
    
    context = {
        'student': student_obj
    }
    return render(request, 'student/update_student.html', context)




def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'student/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'student/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'student/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('home')  
    return render(request, 'student/register.html')




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('home')  # redirect to your home or dashboard page
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'student/login.html')

    return render(request, 'student/login.html')
