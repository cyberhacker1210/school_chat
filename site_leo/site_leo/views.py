from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, "site_leo/index.html", context={"date": datetime.today()})




