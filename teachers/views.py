# Create your views here.
from django.shortcuts import render_to_response

from django.shortcuts import render

from django.http import HttpResponseRedirect

from teachers.models import Message

from django.contrib import auth

from django.contrib.auth.models import User, Group


def inbox(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
	    # Correct password, and the user is marked "active"
	    auth.login(request, user)
	    # Redirect to a success page.
	    return render(request, 'inbox.html',{'user':user})
    else:
		# Show an error page
	    return HttpResponseRedirect("login.html")
def login(request):
    return render(request, 'login.html')
    
def index(request):
	return render(request, 'index.html')

def message(request):
	teacherList = User.objects.filter(groups__name='teachers')
	return render(request, 'message.html', {'teachers':teacherList})
	
def submitted(request):
	username = request.POST.get('teacher','')
	content = request.POST.get('content','')
	if username == '' or content == '':
		return HttpResponseRedirect('/invalidMessage')
	newMessage = Message(username,content)
	return render(request, 'submitted.html')
	
	
