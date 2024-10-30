from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def knowledge_base(request):
    return render(request, "knowledge-base.html")
