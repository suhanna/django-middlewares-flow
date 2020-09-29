from django.shortcuts import HttpResponse


def home(request):
    print("----- Reached View -----")
    return HttpResponse("welcome to Home page")
