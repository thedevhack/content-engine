from django.shortcuts import render


def home(request):
    return render(request, "landing/home.html")


def about(request):
    print(request.project.is_activated)
    return render(request, "landing/home.html")


def error_page(request):
    raise Exception
