import argparse

from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .collect_percentage import main
from .models import Comment, Dustbin
from .forms import CommentForm


@login_required
def all_dustbins(request):
    return render(request, 'datavis/dustbins.html')

@login_required
def get_percentage(request):
    comment = Comment.objects
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('../0/')
    else:
        form = CommentForm()
    return render(
        request,
        'datavis/datavis.html',
        {
            'percentage': main(),
            'comments': comment,
            'form': form,
        }
    )

@login_required
def get_percentage_value(request):
    return HttpResponse(main())

@login_required
def locations(request):
    names = ["Durgapur", "Asansol", "Kolkata"]
    render(request, 'datavis/locations.html', {"names": names})

def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('../0/')
    else:
        form = CommentForm()
    return render(request, 'datavis/add_comment.html', {'form': form})

def view_history(request):
    history = Dustbin.objects
    return render(request, 'datavis/view_history.html', {'history': history})
