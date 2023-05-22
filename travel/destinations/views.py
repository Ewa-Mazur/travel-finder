from django.shortcuts import render, get_object_or_404
from .models import Destination
from django.http import Http404
import random

# Create your views here.


def index(request):
    destinations = Destination.objects.all().order_by('?')[3]
    items = list(Destination.objects.all())
    random_items = random.sample(items,3)

    return render(request, "destinations/index.html", {
        "destinations" : destinations,
        "random_items" : random_items
    })

def all_places(request):
    all_places = Destination.objects.all()
    return render(request, "destinations/all-places.html", {
        "all_places": all_places
    })

def destination_detail(request, slug):
    identified_destination = get_object_or_404(Destination, slug=slug)
    return render(request, "destinations/destination-details.html", {
        "destination" : identified_destination
    })