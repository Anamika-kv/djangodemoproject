from django.contrib import admin
from django.urls import path


from search import views

app_name="search"

urlpatterns = [
    path('',views.searchproducts,name="searchproducts"),
]