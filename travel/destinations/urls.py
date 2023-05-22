from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.index, name="starting-page"), #our-domain.com/destinations
    path("destinations/all-places", views.all_places, name="all-places"),
    path("destinations/<slug:slug>", views.destination_detail, name="destination-detail-page")
]
