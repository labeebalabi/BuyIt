from django.urls import path
from .views import *

urlpatterns=[
    path('new',admin.as_view(),name='adhome'),
    path('addpro',AddProView.as_view(),name='Addpro'),
    path('del/<int:id>',DeleteProView,name='deletepro'),
    path('edit/<int:pk>',Editwork.as_view(),name='editpro'),
    path('notify',NotifyView.as_view(),name='notification'),
    path('addbro',AddBroView.as_view(),name='addbro'),
    path('newbro/<int:id>',NewBro,name='newbro'),
    path('broform',BroAddView.as_view(),name='broform'),
    path('prodel',ProDelView.as_view(),name='prodel'),
    path('plist',ProView.as_view(),name='plist'),
    path('prdel/<int:id>',ProductRequestDelView,name='delrequest'),
    path('delbro/<int:id>',BroDelView,name='delbro'),
    path('editbro/<int:pk>',EditBroker.as_view(),name='editbro')

   
]