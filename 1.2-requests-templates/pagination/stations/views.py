from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        bus_stations_list = list(csv.DictReader(csvfile))
    bus_stations_pagi = Paginator(bus_stations_list, settings.ROWS_PER_PAGE)
    bus_stations = bus_stations_pagi.page(page_number).object_list
    page = bus_stations_pagi.get_page(page_number)
    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
