from django.shortcuts import render
from .models import Planning

# Create your views here.
def planning(request):
    return render(request, "blog/leo.html")

def index(request):
    context = {"plannings": Planning.objects.all()}
    return render(request, "blog/planning.html", context)


