from django.urls import path
from .views import *

urlpatterns=[
    path('reg',UserRegView.as_view(),name='reg'),
     path('logout',logoutView.as_view(),name='ulogout')
]