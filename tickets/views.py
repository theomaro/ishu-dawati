from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "tickets/index.html")


def detail(request, ticket_id):
    return render(request, "tickets/detail.html", {"ticket_id": ticket_id})


def new(request):
    return render(request, "tickets/new.html")
