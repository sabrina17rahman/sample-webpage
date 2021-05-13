from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    name="hello guys"
    return render(request,'base.html',{'name':name})

def tech(request):
    return HttpResponse("Heloo techies!!")    

def getdata(request):
    username=request.GET["username"]
    password=request.GET["password"]
    sab=username+password
    return HttpResponse("  Allow   "+username)

def calculate(request):
    return render(request,'arithmetic.html')

def sabrina(request):
    var1=90
    return render(request,'condition.html',{'var1':var1})
   