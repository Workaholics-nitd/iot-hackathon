import argparse

from django.shortcuts import HttpResponse, render
from .collect_percentage import main

# Create your views here.
def all_dustbins(request):
    return render(request, 'datavis/dustbins.html')

def get_percentage(request):
    return render(request, 'datavis/datavis.html', {'percentage': main()})

def get_percentage_value(request):
    return HttpResponse(main())
