from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class Home(TemplateView):
    template_name="home.html"

class RegView(CreateView):
    template_name='reg.html'
    form_class=RegForm
    model=CustomerUser
    success_url=reverse_lazy('mh')

class LogView(FormView):
    template_name='log.html'
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        r=LogForm(data=request.POST)
        if r.is_valid():
            un=r.cleaned_data.get("username")
            pw=r.cleaned_data.get("password")
            user=authenticate(request,username=un,password=pw)
            if user:
                login(request,user)
                if request.user.usertype=="store":
                    return redirect('sh')
                else:
                    return redirect("ch")
            else:
                return render(request,'log.html',{"form":r})
        else:
            return render(request,'log.html',{"form":r})

