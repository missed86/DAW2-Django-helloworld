# from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponse     # new

# Create your views here.
def home_page_view(request):             # new
    return HttpResponse("¡Hola mundo!")  # new