from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from .forms import BrokerForm
from django.contrib import messages
from Account.models import Broker

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
def signin_required(fn):
    def inner(request,*args,**kwargs):
                if request.user.is_authenticated:
                    return fn(request,*args,**kwargs)
                else:
                     messages.error(request,"login first............")
                     return redirect('log')
                
    return inner

decs = [never_cache,signin_required]
  

# # Create your views here.

@method_decorator(decs,name='dispatch')
class BrokerAddView(CreateView):
    template_name='Badd.html'
    form_class=BrokerForm
    model=Broker
    success_url=reverse_lazy('Bhome')
    
    def form_valid(self, form):
        messages.success(self.request, 'Request created successfully!!  We will Contact you Soon!!')

        return super().form_valid(form)