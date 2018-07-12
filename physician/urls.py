from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'doctors',views.doctors_list),
]