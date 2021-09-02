from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def terms(request):
    return render(request,"terms.html")

def Login(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Crediantials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    


def register(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        password2=request.POST['re_pass']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password mismatched')
            return redirect('register')
    else:
        return render(request,'register.html')
    

            


