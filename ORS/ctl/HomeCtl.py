
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render


class HomeCtl(BaseCtl):

    def display(self,request,params={}):
       
        return render(request,self.get_template())

    def submit(self,request,params={}):
        return render(request,self.get_template(),{"form":self.form})

  
    def get_template(self):
        return "ors/Home.html"        

  
    def get_service(self):
        return "RoleService()"        
