from django.urls import path,include
from broker import urls
from .views import *

urlpatterns=[
    path('home',BuyHomeView.as_view(),name='Bhome'),
    path('pro',PropertyView.as_view(),name="property"),
    path('bro',BrokerView.as_view(),name="brokers"),
    path('detail/<int:id>',DetailView.as_view(),name='Detail'),
    path('wish/<int:id>',AddWish,name='add'),
    path('pay/<int:id>',PayView.as_view(),name='pay'),
    path('wish',WishListView.as_view(),name='wish'),

    path('br/',include('broker.urls')),
    path('delwish/<int:id>',DeleteWish,name='delwish')



]