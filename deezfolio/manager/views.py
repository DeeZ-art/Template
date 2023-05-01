from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from core.models import Portfolio,Contact
import os
# Create your views here.
def manager(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("panel")
        else:
            messages.error(request,'Username or Password entered is incorrect, Please Check!!')
            return redirect("manager")
        
    return render(request,'manager.html')
def panel(request):
    return render(request,'panel.html')
def Logout(request):
    logout(request)
    return redirect('index')
def portfolio(request):
    portfolio=Portfolio.objects.all()
    context = {'portfolio':portfolio}
    return render(request,'portfolio.html',context)
def addport(request):
    if request.method=="POST":
        image=request.POST.get('image')
        heading=request.POST.get('heading')
        description=request.POST.get('description')
        filter=request.POST.get('filter')

        if len(request.FILES)!=0:
            image=request.FILES['image']

        addport=Portfolio(
            image=image,
            heading=heading,
            description=description,
            filter=filter
        )
        addport.save()
        return redirect('portfolio')

    return render(request,'portfolio.html')
def editport(request,pk):
    port = Portfolio.objects.get(id=pk)
    if request.method == "POST":
        # to check whether there is a file or not
        if len(request.FILES) != 0:
            # to check whether there is an image or not 
            if len(port.image) > 0:
                # if there is an image it will remove the previous one
                os.remove(port.image.path)
            port.image = request.FILES['image']
        port.heading = request.POST.get('heading')
        port.description = request.POST.get('description')
        port.filter = request.POST.get('filter')

        port.save()
        return redirect('portfolio')
    context = {"port":port}
    return render(request,'portfolio.html',context)
def deleteport(request,pk):
    port = Portfolio.objects.get(id = pk)
    if len(port.image) > 0:
        # if there is an image it will remove the previous one
        os.remove(port.image.path)
    port.delete()
    context = {'port':port}
    return redirect('portfolio')
    