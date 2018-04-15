from .models import Idea, Comments, Like
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime
# Views here


# First page
@login_required(redirect_field_name='login_render')
def index(request):
    user_set = User.objects.get( username = request.user )
    return render(request,'webapp/home.html', {'user_set':user_set})

#Login data taken
def loginreq(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(username = user, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            error_message = 'invalid credentials'
            return render(request,'webapp/error.html',{'error_message':error_message})
    else:
        error_message = 'This is not a valid request'
        return render(request,'webapp/error.html',{'error_message':error_message})

#Renders Login Page
def login_render(request):
    return render(request,'webapp/ll.html')

#Function of logout button
@login_required(redirect_field_name='login_render')
def logoutrender(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_render'))

#Renders Registration Page
def register_render(request):
        return render(request,'webapp/register.html')


def creates(request):
    queryset = Idea.objects.all()
    user = User.objects.get(username=request.user.username)
    if request.method =='POST':
        if queryset.filter(subject = request.POST.get('subject')):
            error_message = 'This subject already exists'
            return render(request, 'webapp/error.html', {'error_message':error_message})
        else:
            subject = request.POST.get('subject')
            Idea.objects.create(subject = subject ,text=request.POST.get('body'), user = user)
            #query=idea.objects.all().filter(subject = request.POST['subject'])
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'webapp/newpost.html', {})


def viewIdeas(request, pk):
    try:
        queryset = Idea.objects.all().get(pk= pk)
        Comms = Comments.objects.all().filter(ideas = queryset).order_by('-date_time')
    except Idea.DoesNotExist:
        raise Http404("Post does not exist")
    else:

        return render(request,'webapp/ideas.html',{'queryset':queryset,'Comms':Comms})
   
def likePost(request, pk):
    if True:
        user = User.objects.get(username=request.user.username)
        if request.user is not None:
            try:
                queryset = Like.objects.get(user = user,ideas = Idea.objects.get(pk = pk) )
            except Like.DoesNotExist:
                Like.objects.create(user= user, ideas = Idea.objects.get(pk = pk))
            
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            logout(request)
            return render(request,'webapp/ll.html') 
    else:
        raise Http404("This is a violation of our terms to use invalid requests")

def commentPost(request, pk):
    if request.method == 'POST' :
        user = User.objects.get(username=request.user.username)
        if request.user is not None:
            try:
                queryset = Comments.objects.get(user = user,ctext = request.POST['comment'])
            except Comments.DoesNotExist:
                Comments.objects.create(user= user, ideas = Idea.objects.get(pk = pk),ctext=request.POST['comment'])
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            logout(request)
            return render(request,'webapp/ll.html') 
    else:
        raise Http404("This is a violation of our terms to use invalid requests")


def ideas(request):
    queryset = Idea.objects.all().order_by('-date_time')[:5]
    
    return render(request, 'webapp/allideas.html', {'queryset':queryset})