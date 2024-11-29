"""
URL configuration for my_loan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Signup),
    path('pan/', views.Panpage),
    
    path('notpan/', views.Notpan),
    path('mail/', views.Mail),
    path('gift/', views.Gift),
    path('load/', views.Load),
    path('inform/', views.Inform),
    path('ref/', views.Ref),
    path('loan/', views.Loan),
    path('savephone/', views.Savephone,name="savephone"),
    path('savemail/', views.Savemail,name="savemail"),
    path('pansave/', views.Pansave,name="pansave"),
    path('nopan/', views.NoPansave,name="nopan"),
    path('payment/', views.Pay,name="payment"),
    path('loanhit/', views.Loanhit,name="loanhit"),
    path('inref/', views.Inref,name="inref"),
    path('refpay/', views.Refpay,name="refpay"),
    path('testupi/', views.Testupi,name="testupi"),
    path('ifnotpan/', views.IfNotpan,name="ifnotpan"),
    path('delete-all-records/',views.delete_all_records, name='delete_all_records'),
    
]
