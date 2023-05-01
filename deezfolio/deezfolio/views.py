from unicodedata import name
from django.shortcuts import render
from django.contrib import messages
from core.models import Portfolio,Contact
# Create your views here.

def index(request):
    portfolio=Portfolio.objects.all()
    context = {'portfolio':portfolio}

    # for contact page
    if request.method=="POST":
        contact = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message')
        )
        contact.save()
        messages.success(request,'Your message has been sent succesfully, Thank You!')
    return render(request,'index.html',context)
def contact(request):
    return render(request,'contact.html')