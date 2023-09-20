from django.shortcuts import render
from .models import Planning
from django.db.models import Case, When, Value, IntegerField, Count

# Create your views here.
def planning(request):
    return render(request, "blog/leo.html")

# def index(request):
#     jours_order = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
#     heures_distinctes = ['8h30', '9h30', '10h30', '11h30', '12h30', '13h30', '14h30', '15h30']
#     jour_distinctes = Planning.objects.values('jour').annotate(Count('id')).order_by('jour')
#     context = {"plannings": Planning.objects.all(), 'jour_distinctes': jour_distinctes, 'heures_distinctes': heures_distinctes}
#     return render(request, "blog/planning.html", context)


def index(request):
    jours_order = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    heures_distinctes = ['8h30', '9h30', '10h30', '11h30', '12h30', '13h30', '14h30', '15h30']
    # Utiliser Case et When pour définir l'ordre de tri personnalisé
    preserved = Case(*[When(jour=jour, then=Value(pos)) for pos, jour in enumerate(jours_order)],
                         output_field=IntegerField())

    jour_distinctes = Planning.objects.values('jour').annotate(Count('id')).annotate(sort_order=preserved).order_by(
            'sort_order')

    context = {"plannings": Planning.objects.all(), 'jour_distinctes': jour_distinctes,
                   'heures_distinctes': heures_distinctes}
    return render(request, "blog/planning.html", context)

