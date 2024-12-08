from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from datetime import date
# Create your views here.
def index(request):
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html",locals())


