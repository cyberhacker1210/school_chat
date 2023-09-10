from django.shortcuts import render
from .models import Planning
from django.db.models import Count

# Create your views here.
def planning(request):
    return render(request, "blog/leo.html")

def index(request):
    jour_distinctes = Planning.objects.values('jour').annotate(Count('id')).order_by('jour')
    context = {"plannings": Planning.objects.all(), 'jour_distinctes': jour_distinctes}
    return render(request, "blog/planning.html", context)