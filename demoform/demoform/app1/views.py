from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from app1.models import student
from django.http import HttpResponse
from app1.forms import studentform
def home(request):
    return render(request,'home.html',{'name':'pranav','age':21})

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("ABout")

def relative(request):
    return render(request,'relative.html')

def viewdetails(request):
    k=student.objects.all()
    return render(request,'list.html',{'s':k})

def form1(request):
    form=studentform() #empty form object
    if(request.method=="POST"):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return viewdetails(request)
    return render(request,'form1.html',{'f':form})


