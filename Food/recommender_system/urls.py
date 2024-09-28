from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("<int:recipe_id>/details/", views.details_page, name="details_page")

]
