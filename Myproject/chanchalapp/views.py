from django.shortcuts import render,redirect
from chanchalapp.models import*
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def ragistration(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Emial Is alredy exits")
        elif User.objects.filter(phone=phone).exists():
            return HttpResponse("Phone Number is alredy exists")
        else:
            User.objects.create(name=name,email=email,phone=phone,password=password)
            return HttpResponse("User cretae")

# Create your views here.

def table(request):
    data =User.objects.all()
    return render(request,'table.html',{"data":data})

def userdelete(request,pk):
    User.objects.get(id=pk).delete()
    return redirect('/table/')


