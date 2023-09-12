from django.urls import path
from .views import *

urlpatterns=[
    path('Breg',BrokerAddView.as_view(),name='Brokeradd')
]