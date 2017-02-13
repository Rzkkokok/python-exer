from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from models import User
class Userform(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

def h20(request):
	if request.method == 'POST':
		uf = Userform(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			print(username,password)
			User.objects.create(username = username,password = password)
			return HttpResponseRedirect('/login/')
	else:
		uf = Userform()
	return render(request,'h20.html',{'uf':uf})

def login(request):
        if request.method == 'POST':
                uf = Userform(request.POST)
                if uf.is_valid():
                        username = uf.cleaned_data['username']
                        password = uf.cleaned_data['password']
                        print(username,password)
                        users = User.objects.filter(username__exact = username,password__exact = password)
                        if users:
				reponse = HttpResponseRedirect('/index')
				request.session['username'] = username
                       		return reponse
        else:
                	uf = Userform()
        return render(request,'login.html',{'uf':uf})

def index(request):
	username = request.session.get('username','')
	return render(request,'index.html',{'username':username})

def logout(request):
	del request.session['username']
	return HttpResponse('ok')


# Create your views here.
