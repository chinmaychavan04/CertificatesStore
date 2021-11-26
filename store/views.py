import collections
from django.contrib.auth import authenticate,login, logout
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='login')
def home(request):    
    categaryID=request.GET.get('catagory')
    obj=Collection.objects.filter(fields_id=categaryID)
    context={
        'obj':obj,
        }
    return render(request,'home.html',context)

@login_required(login_url='login')
def field(request):
    cat=Catagory.objects.all()
    context={'cat':cat}
    return render(request,'fields.html',context)  

@login_required(login_url='login')
def search(request):
    query=request.GET.get('search')
    object=Collection.objects.filter(Q(title__icontains=query)|Q(fields__fields__icontains=query))
    context={
        'object':object,
    'query':query
    }
    return render(request,'search.html',context) 


def search_list(request):
    query=request.GET.get('slist')
    object=Collection.objects.filter(Q(title__icontains=query)|Q(fields__fields__icontains=query))
    context={
        'object':object,
    'query':query
    }
    return render(request,'search_list.html',context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('field')
            return redirect('field')    
		
        else:
            return render(request, 'login.html')

    return render(request,'login.html')  


def logoutUser(request):
	logout(request)
	return redirect('/login')           

@login_required(login_url='login')
def add_post(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('all_list')
        else:
            return redirect('')    
    context ={'form':form}
    return render(request,'forms.html', context)


@login_required(login_url='login')
def all_list(request):
    posts=Collection.objects.all().order_by("-title")
    context ={'posts':posts}
    return render(request,'lists.html',context)   


@login_required(login_url='login')
def delete_post(request,id):
    try:
        obj=Collection.objects.get(id=id)
        obj.delete()
    except Exception as e:
        print(e)
    return redirect('/list')    