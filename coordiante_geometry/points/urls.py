from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path('p1', views.upsert, name='upsert'),
    re_path('p2', views.average, name='average'),

]