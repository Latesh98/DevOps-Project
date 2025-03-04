from django.shortcuts import *
from .models import recepies,User # fsfs
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login/")       #Decorator for login until login no one cna access recepeies
def recepies_view(request):
    queryset=recepies.objects.all()
    success=False 
    if request.method=='POST':
        recepie_name=request.POST.get('recepie_name')
        recepie_description=request.POST.get('recepie_description')
        recepie_img=request.FILES.get('recepie_img')

        if recepies.objects.create(recepie_name=recepie_name,recepie_description=recepie_description,recepie_img=recepie_img):
            success=True

        return redirect('/recepies/')
    if(request.GET.get('search')):
        queryset=queryset.filter(recepie_name__icontains=request.GET.get('search'))
        
    return render(request, 'recepies.html',context= {
            'recepies': queryset,
            # 'success': success,  # Pass success context to the template
        })
    
@login_required(login_url="/login/") 
def update_recepies(request,id):
    queryset=recepies.objects.get(id=id)
    if request.method=='POST':
        recepie_name=request.POST.get('recepie_name')
        recepie_description=request.POST.get('recepie_description')
        
        recepie_img=request.FILES.get('recepie_img')

        queryset.recepie_name=recepie_name
        queryset.recepie_description=recepie_description
        if recepie_img:
            queryset.recepie_img=recepie_img
        
        queryset.save()
        return redirect('/recepies/')
    return render(request, 'update_recepies.html',context= {
            'recepie': queryset,
            # 'success': success,  # Pass success context to the template
        })

@login_required(login_url="/login/") 
def delete_recepies(request,id):
    todel=recepies.objects.get(id=id)
    todel.delete()
    return redirect('/recepies/')

def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/recepies/')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request,'login_page.html')
    return render(request, 'login_page.html')
    # queryset=
    # if request.method == 'POST':

    
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if all fields are filled
        if not all([username, email, password, confirm_password]):
            messages.info(request, 'ALL FIELDS ARE REQUIRED')
            return redirect('/register')
        
        # Check if the user already exists
        user = User.objects.filter(username=username).first()
        if user:
            messages.info(request, 'USERNAME NOT AVAILABLE')
            return redirect('/register')
        
        # Check if passwords match
        if password != confirm_password:
            messages.info(request, 'PASSWORDS DO NOT MATCH')
            return redirect('/register')
        
        # Create the new user
        user = User(username=username, email=email)
        user.set_password(password)  # Hash the password inbuilt method
        user.save()
        
        messages.info(request, 'USER ADDED SUCCESSFULLY')
        # return redirect('/login')
    
    return render(request, 'register_page.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')