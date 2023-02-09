from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homePg(request):
    return render(request,"index.html")


def aboutUs(request):
    return render(request,"AboutUs.html")

def Donor_signin(request):
    return render(request,"Donor-signin.html")

def NGO_Signin(request):
    return render(request,"NGO-signin.html")

def courses(request):
    return HttpResponse("Here courses will be displayed")

def courseId(request,cid):
    return HttpResponse(cid)