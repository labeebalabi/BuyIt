# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,View,UpdateView
from Account.models import Property,Booking,Broker
from .forms import PropertyForm
from broker.forms import BrokerForm
from django.urls import reverse_lazy
from buyers.views import BrokerView
# from buyers.urls import BrokerView
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
  

# Create your views here.


@method_decorator(decs,name='dispatch')
class admin(TemplateView):
    template_name='adhome.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     # Retrieve the count of items from your model
    #     item_count = Booking.objects.count()
    #     item_count_bro = Broker.objects.filter(status=0).count()

        
    #     context['item_count_pro'] = item_count
    #     context['item_count_bro'] = item_count_bro
    #     return context
@method_decorator(decs,name='dispatch')
class AddProView(CreateView):
    template_name='addpro.html'
    form_class=PropertyForm
    model=Property
    success_url=reverse_lazy('adhome')


decs
def DeleteProView(request,**kwargs):
    pid=kwargs.get('id')
    print(pid)
    c=Property.objects.get(id=pid)
    print(c)
    c.delete()

    # messages.success(request,'Cart item removed....')
    return redirect('adhome')

@method_decorator(decs,name='dispatch')
class ProDelView(ListView):
    template_name='delpro.html'
    queryset = Property.objects.all()
    context_object_name = 'Property'

@method_decorator(decs,name='dispatch')
class NotifyView(ListView):
    template_name='notify.html'
    queryset=Booking.objects.all()
    context_object_name='order'

@method_decorator(decs,name='dispatch')
class AddBroView(ListView):
    template_name='addbro.html'
    queryset=Broker.objects.all()
    context_object_name='order'

decs
def NewBro(request,**kwargs):
    id=kwargs.get('id')
    c=Broker.objects.get(id=id)
    c.status=1
    c.save()
    return redirect('addbro')

@method_decorator(decs,name='dispatch')
class BroAddView(CreateView):
    template_name='broform.html'
    form_class=BrokerForm
    model=Broker
    success_url=reverse_lazy('brokers')

@method_decorator(decs,name='dispatch')
class ProView(ListView):
    template_name='plist.html'
    queryset = Property.objects.all()
    context_object_name = 'Property'

  
class Editwork(UpdateView):

    model = Property
    form_class = PropertyForm
    template_name = 'addpro.html'
    success_url = reverse_lazy('adhome')  # Replace 'success_url_name' with the actual URL name

    def form_valid(self, form):
        # Handle form submission here
        # Save the updated data and images
        return super().form_valid(form)
    # def get(self,request,*args,**kwargs):
    #     pid=kwargs.get("id")
    #     ob=Property.objects.get(id=pid)
    #     form=PropertyForm(instance=ob)
    #     return render(request,"addpro.html",{"form":form})
  
    # def post(self,request,*args,**kwargs):
    #     eid=kwargs.get("id")
    #     ob=Property.objects.get(id=eid)
    #     form_data=PropertyForm(data=request.POST,instance=ob)
    #     if form_data.is_valid():
                       
    #                    form_data.save()
    #                    return redirect('adhome')
    #     return render(request,"addpro.html",{"form":form_data})
    

decs
def ProductRequestDelView(request,**kwargs):
    prid=kwargs.get('id')
    x=Booking.objects.get(id=prid)
    x.delete()
    return redirect('notification')


from django.urls import reverse
decs
def BroDelView(request,**kwargs):
    brid=kwargs.get('id')
    x=Broker.objects.get(id=brid)
    x.delete()
    # return redirect(request.path)
    return redirect('brokers')

class EditBroker(UpdateView):

    model = Broker
    form_class = BrokerForm
    template_name = 'broform.html'
    success_url = reverse_lazy('brokers')  # Replace 'success_url_name' with the actual URL name

    def form_valid(self, form):
        # Handle form submission here
        # Save the updated data and images
        return super().form_valid(form)