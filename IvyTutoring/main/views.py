from django.http import JsonResponse, Http404, HttpResponse
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .forms import *
import json

def HomePage(request):
	return render(request, 'main/home.html')

def ParentReg(request):
	if request.method == 'POST':
		form = ParentForm(request.POST)
		if form.is_valid():
			user = form.save()
			if Group.objects.filter(name='Parent'):
				group = Group.objects.get(name='Parent')
				user.groups.add(group)
			else:
				Group.objects.create(name='Parent')
				group = Group.objects.get(name='Parent')
				user.groups.add(group)
		else:
			print(form.errors)
		return redirect('/login')
	else:
		form = ParentForm() 
		context = {'form': form }
		return render(request, 'main/signup.html', context)

def StudentReg(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			user = form.save()
			if Group.objects.filter(name='Student'):
				group = Group.objects.get(name='Student')
				user.groups.add(group)
			else:
				Group.objects.create(name='Student')
				group = Group.objects.get(name='Student')
				user.groups.add(group)
		else:
			print(form.errors)
		return HttpResponse("Registered")
	else:
		form = StudentForm() 
		context = {'form': form }
		return render(request, 'main/signup.html', context)

def TutorReg(request):
	if request.method == 'POST':
		form = TutorForm(request.POST)
		if form.is_valid():
			user = form.save()
			if Group.objects.filter(name='Tutor'):
				group = Group.objects.get(name='Tutor')
				user.groups.add(group)
			else:
				Group.objects.create(name='Tutor')
				group = Group.objects.get(name='Tutor')
				user.groups.add(group)
		else:
			print(form.errors)
		return HttpResponse("Registered")
	else:
		form = TutorForm() 
		context = {'form': form }
		return render(request, 'main/signup.html', context)

def UserLogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.user_type == 1:
				login(request, user)
				return render(request, 'main/parent.html')
			elif user.user_type == 2:
				login(request, user)
				return render(request, 'main/student.html')
			elif user.user_type == 3:
				login(request, user)
				return render(request, 'main/tutor.html')
		else:
			return render(request, 'main/login.html')
	else:
		return render(request, 'main/login.html')