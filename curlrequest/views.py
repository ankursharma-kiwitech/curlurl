from django.shortcuts import render
from .forms import url


# Create your views here.
def home_view(request):

    return render(request, "home.html")
