from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse



def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==c):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
        else:
            return HttpResponse("password should be same")
        return redirect('books:home')

    return render(request,'register.html')


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('users:login')