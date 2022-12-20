from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('booking/',views.booking,name="booking"),
    path('doctors/',views.doctors,name="doctors"),
    path('departments/',views.departments,name="departments"),
    path('contactus/',views.contactus,name="contactus"),
]