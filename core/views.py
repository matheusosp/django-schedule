from django.shortcuts import render, redirect, HttpResponse
from core.models import event
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse 
from django.contrib.auth.models import User


@login_required(login_url='/login/')
def list_events(request):
    user = request.user
    date_now = datetime.now() - timedelta(hours=1)
    Event =event.objects.filter(user=user,data_event__gt=date_now)
    data = {'events':Event}
    return render(request, 'schedule.html',data)


def login_user(request):
    return render(request,'login.html')     


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalidos!")
    return redirect('/')


@login_required(login_url='/login/')
def schedule_new(request):
    id_event = request.GET.get('id')
    data = {}
    if id_event:
        data['event'] = event.objects.get(id=id_event)   
    return render(request, 'event.html', data)


@login_required(login_url='/login/')
def event_submit(request):
    if request.POST:
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')
        local = request.POST.get('local')
        username = request.user
        id_event = request.POST.get('id_event')
        if id_event:
            Event = event.objects.get(id=id_event)
            if Event.user == username:
                Event.title=title
                Event.data_event=date
                Event.description=description
                Event.local=local
                Event.save()
        else:
            event.objects.create(title=title, data_event=date, description=description, user=username,local=local)
    return redirect('/')


@login_required(login_url='/login/')
def delete_event(request, id_event):
    username = request.user
    try:
        Event = event.objects.get(id=id_event)
    except Exception:
        raise Http404()
    if username == Event.user:
        Event.delete()
    else:
        raise Http404()    
    return redirect('/')


@login_required(login_url='/login/')
def json_list_events(request, id_user):
    username = User.objects.get(id=id_user)
    user = request.user
    Event =event.objects.filter(user=username).values('id','title')
    return JsonResponse(list(Event), safe=False)  



#def index(request):
#    return redirect('/agenda/')    