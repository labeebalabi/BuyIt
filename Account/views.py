from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView,View
from .forms import LoginForm,NewUser

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.

class LoginView(FormView):
    template_name="loginpage.html"
    form_class = LoginForm
    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user = authenticate(request,username=uname,password=pswd)
            if user:
                # login(request,user)
                if user.is_superuser:

                    login(request,user)
                    messages.success(request,"login successfully")
                    return redirect('adhome')
                else:
                    login(request,user)
                    messages.success(request,"login successfully")
                    return redirect('Bhome')

            else:
                messages.error(request,"login unsuccessfully")
                return redirect('log')
        return render(request,'loginpage.html',{'form':form_data})


class UserRegView(CreateView):
    template_name='registration.html'
    form_class=NewUser
    model=User
    success_url=reverse_lazy('log')
    def form_valid(self,form):
        messages.success(self.request,"registration completed")
        return super().form_valid(form)


class logoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('log')
    
