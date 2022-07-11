from django.shortcuts import render,redirect
from django.http import HttpResponse
from bank.models import Reclog
from bank.forms import stform
from django.contrib import messages
def index(request):
    return render(request,"home.html")
def transaction(request):
    if request.method=="POST":
        if request.POST.get('AccountName') and request.POST.get('AccountNumber') and request.POST.get('Amt') and request.POST.get('currency') :
            savest=Reclog()
            savest.Recname=request.POST.get('AccountName')
            savest.Recno=request.POST.get('AccountNumber')
            savest.Amt=request.POST.get('Amt')
            savest.Curr=request.POST.get('currency')
            savest.save()
            messages.success(request,'Transaction created successfully')
            return render(request,"transaction.html",{"Name":savest.Recname,"AccountNum":savest.Recno,"qr":'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/640px-QR_code_for_mobile_English_Wikipedia.svg.png'})
    else:
        return render(request,"transaction.html")
