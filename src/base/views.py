from django.shortcuts import render, redirect
from .forms import RUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import RUser, Link
import json
import random
from .unique_id_gen import snowflake
from .baseConv import encode, decode
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def tempRedirect(request,url):
    link_id = decode(url)
    try:
        link = Link.objects.get(link_id=link_id)
        requested_url = link.original_url
    except Link.DoesNotExist:
        return render(request, 'base/404.html' ,{'url':url})
    return HttpResponseRedirect(requested_url)

def registerUser(request):
    form = RUserCreationForm()
    if request.method == 'POST':
        form = RUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.name.lower()
            user.save()
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, 'An error occurred during registration')
        

    context = {'form':form}
    return render(request, 'base/register.html', context)

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def loginUser(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = RUser.objects.get(email=email)
    except:
        messages.error(request,'user does not exist')
    user = authenticate(request,email=email,password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        messages.error(request,'email or password incorrect')
    context = {}
    return render(request, 'base/login.html', context)
def ajax_url(request):
    if request.method == 'POST':
        user = request.user
        post_data = json.loads(request.body.decode('utf-8'))
        original_url = post_data['url']
        maching_id = random.randint(0,12)
        datacenter_id = random.randint(0,12)
        link_id = snowflake(
            machine_id=maching_id,
            datacenter_id=datacenter_id
        )
        url_str = encode(link_id)
        try:
            Link.objects.create(
                user=user,
                original_url =original_url,
                link_id=link_id
            )
        except:
            messages.error(request,'something went wrong when creating short link')
        return HttpResponse(json.dumps({'short_url': url_str}), content_type='application/json')
    





@login_required(login_url='login')
def renderProfile(request):
    context = {}
    return render(request, 'base/profile.html', context)

