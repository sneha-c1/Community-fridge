"""
URL configuration for communityfridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from communityapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('userregister',views.userregister,name='userregister'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('donation',views.donationitems,name='donation'),
    path('profile',views.profile,name='profile'),
    path('donationhistory',views.donation_history,name='donationhistory'),
    path('donateitem',views.donation_items,name='donateitem'),
    path('fooditems',views.fooditems,name='fooditems'),
    path('clotheitems',views.clothitems,name='clotheitems'),
    path('requestitem',views.requestitems,name='requestitem'),
    path('personal',views.personal,name='personal'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('requesthistory',views.requesthistory,name='requesthistory'),
    path('driverlogin',views.driverlogin,name='driverlogin'),
    path('driverprofile',views.driverprofile,name='driverprofile'),
    path('deliveredupdate/<str:place>',views.deliveredupdate,name='deliveredupdate'),
    path('onthewayupdate/<str:place>',views.onthewayupdate,name='onthewayupdate'),
    path('deletedonateitem/<int:id>',views.deletedonateitem,name='deletedonateitem'),
    path('deleterequestitem/<int:id>',views.deleterequestitem,name='deleterequestitem'),
    path('statusupdate/<int:id>',views.statusupdate,name='statusupdate'),
    path('status1update/<int:id>',views.status1update,name='status1update'),
]
