from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect

class Userform(forms.Form):
	username = forms.CharField()
	
def h20(request):
	if request.method == 'POST':
		uf = Userform(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			request.session['username'] = username
			print(username)
			return HttpResponseRedirect('/index')
	else:
		uf = Userform()
	return render(request,'h20.html',{'uf':uf})

def index(request):
	username = request.session.get('username','anybody')
	return render(request,'index.html',{'username':username})

def logout(request):
	del request.session['username']
	return HttpResponse('ok')


# Create your views here.
