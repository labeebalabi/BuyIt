from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,View
from Account.models import Property,Like,Booking,Broker
from django.contrib import messages
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

# class BuyHomeView(TemplateView):
#     template_name='buyerhome.html'

@method_decorator(decs,name='dispatch')
class BuyHomeView(View):
    def get(self,request):
        return render(request,'buyerhome.html')

@method_decorator(decs,name='dispatch')
class PropertyView(ListView):
    template_name='property.html'
    queryset = Property.objects.all()
    context_object_name = 'Property'

@method_decorator(decs,name='dispatch')
class BrokerView(ListView):
    template_name='brokers.html'
    queryset=Broker.objects.all()
    context_object_name='Brokerdet'

@method_decorator(decs,name='dispatch')
class DetailView(DetailView):
    template_name='details.html'
    pk_url_kwarg='id'
    context_object_name='specific'
    queryset=Property.objects.all()



decs
def AddWish(request,**kwargs):
    id=kwargs.get("id")
    wishl=Property.objects.get(id=id)
    user=request.user
    # if Like.objects.get()
    print(user)
    print(wishl)
    entry=Like.objects.filter(user=user,propery=wishl)
    if not entry:
         
        Like.objects.create(propery=wishl,user=user)
        messages.success(request,'Added to Wishlist.........')
    else:
         messages.info(request,'Already existing in Wishlist.........')
 
    return redirect('property')

@method_decorator(decs,name='dispatch')
class PayView(TemplateView):
    template_name='payment.html'
    def post(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get('id')
        pro=Property.objects.get(id=id)
        ph=request.POST.get('phone')
        rs=request.POST.get('amt')
        
        # if int(rs) == 50:
        Booking.objects.create(user=user,propery=pro,phone=ph,price=rs)
        messages.success(request,'Order Successfully Registered!.... We Will Contact You Soon!!')
            
        return redirect('Bhome')
        # else:
        #     messages.error(request,'The amount should be 50 Rupees')
            
        #     return render(request,'payment.html')

        # # return redirect('Bhome')

@method_decorator(decs,name='dispatch')
class WishListView(ListView):
     template_name='wishlist.html'
     queryset=Like.objects.all()
     context_object_name='like'

decs
def DeleteWish(request,**kwargs):
    pid=kwargs.get('id')
    print(pid)
    c=Like.objects.get(id=pid)
    print(c)
    c.delete()

    # messages.success(request,'Cart item removed....')
    return redirect('wish')
