from django.shortcuts import render
from .models import Departments,Doctors
from .forms import Bookingform


def departments(request):
    dict_dpt={
        'dept':Departments.objects.all()
    }
    print(dict_dpt)
    return render(request,'departments.html',dict_dpt)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def booking(request):
    form = Bookingform()
    dict_form ={
        'form': form
    }
    return render(request,'booking.html',dict_form)


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')
    
