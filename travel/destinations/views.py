from django.shortcuts import render, get_object_or_404
from .models import Destination
from django.http import Http404
from .forms import LocationForm
import random
from django.db.models import Q
from functools import reduce
import operator

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

def travel_search(request):
    destinations = Destination.objects.all()
    search_result = None
    price_filters = []
    temp_filters = []
    #continent_filters = []

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
                
            selected_prices = form.cleaned_data['hotel_price']
            selected_temperatures = form.cleaned_data['temperature']
            selected_continents = form.cleaned_data['continent']
    

            for option in selected_prices:
                if option == '1':
                    price_filters.append(Q(hotel_price__gte=0, hotel_price__lte=50))
                elif option == '2':
                    price_filters.append(Q(hotel_price__gte=50, hotel_price__lte=75))
                elif option == '3':
                    price_filters.append(Q(hotel_price__gte=75, hotel_price__lte=100))
                elif option == '4':
                    price_filters.append(Q(hotel_price__gte=100))


            for option in selected_temperatures:
                if option == '1':
                    temp_filters.append(Q(avg_year_temp__gte=0, avg_year_temp__lte=10))
                elif option == '2':
                    temp_filters.append(Q(avg_year_temp__gte=10, avg_year_temp__lte=15))
                elif option == '3':
                    temp_filters.append(Q(avg_year_temp__gte=15, avg_year_temp__lte=20))
                elif option == '4':
                    temp_filters.append(Q(avg_year_temp__gte=20, avg_year_temp__lte=25))
                elif option == '5':
                    temp_filters.append(Q(avg_year_temp__gte=25))

            # Inicjalizuj filtr pusty
            continent_filters = Q()

            # Iteruj przez wybrane kontynenty i dodawaj warunki filtrowania
            for continent_name in selected_continents:
                continent_filters |= Q(continent__name=continent_name)
            

            is_beach_value = form.cleaned_data["is_beach"]
            are_mountains_value = form.cleaned_data["are_mountains"]

            if "reset_filters" in request.POST:
                # Jeśli przycisk "Resetuj" został kliknięty, zresetuj wartości filtrów
                form = LocationForm()  # Tworzy nowy pusty formularz
            else:
                # Obsługa filtrowania i innych działań

                if price_filters:
                    search_result = Destination.objects.filter(
                        reduce(operator.or_, price_filters)
                    )
                else:
                    search_result = Destination.objects.all()


                if is_beach_value == 'None':
                    pass
                else:
                    search_result = search_result.filter(Q(is_beach=is_beach_value))

                if are_mountains_value == 'None':
                    pass
                else:
                    search_result = search_result.filter(Q(are_mountains=are_mountains_value))

                if temp_filters:
                    search_result = search_result.filter(
                        reduce(operator.or_, temp_filters)
                    )
                
                if continent_filters:
                    search_result = search_result.filter(continent_filters)



            #print(form.cleaned_data["is_beach"])
            #print(form.cleaned_data["continent"])

    else:
        form = LocationForm()

    return render(request, "destinations/travel-search.html", {
        "form" : form,
        "destinations" : destinations,
        "search_result" : search_result
    })