from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("All Tickets")


def detail(request, ticket_id):
    return HttpResponse(f"Ticket #{ticket_id}")


def new(request):
    return HttpResponse("New Ticket")
