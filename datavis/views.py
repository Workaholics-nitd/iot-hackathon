import argparse

from django.shortcuts import HttpResponse, render
from .quickstart import main

# Create your views here.
def get_percentage(request):
    return render(request, 'datavis/datavis.html', {'percentage': main()})

def get_percentage_value(request):
    return HttpResponse(main())

def all_dustbins(request):
    return render(request, 'datavis/dustbins.html')
