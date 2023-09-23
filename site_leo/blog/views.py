import datetime
from .models import Planning
from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField, Count

# Create your views here.
def planning(request):
    return render(request, "blog/leo.html")

def est_semaine_paire(date):
    # Obtenir le numéro de la semaine pour la date fournie
    semaine_num = date.isocalendar()[1]
    return semaine_num % 2 == 0

date_actuelle = datetime.date.today()


# def index(request):
#     jours_order = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
#     heures_distinctes = ['8h30', '9h30', '10h30', '11h30', '12h30', '13h30', '14h30', '15h30']
#     preserved = Case(*[When(jour=jour, then=Value(pos)) for pos, jour in enumerate(jours_order)],
#                          output_field=IntegerField())
#     jour_distinctes = Planning.objects.values('jour').annotate(Count('id')).annotate(sort_order=preserved).order_by(
#             'sort_order')
#     if est_semaine_paire(date_actuelle):
#         semaine_paire = Planning.objects.filter(q1__in=["0", "1"])
#         context = {"plannings": Planning.objects.all(), 'jour_distinctes': jour_distinctes,
#                    'heures_distinctes': heures_distinctes, 'semaine_paire': semaine_paire}
#     else:
#         semaine_impaire = Planning.objects.filter(q1__in=["0", "2"])
#         context = {"plannings": Planning.objects.all(), 'jour_distinctes': jour_distinctes,
#                    'heures_distinctes': heures_distinctes, 'semaine_impaire': semaine_impaire}
#
#     return render(request, "blog/planning.html", context)



def index(request):
    jours_order = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    heures_distinctes = ['8h30', '9h30', '10h30', '11h30', '12h30', '13h30', '14h30', '15h30']

    preserved = Case(*[When(jour=jour, then=Value(pos)) for pos, jour in enumerate(jours_order)], output_field=IntegerField())
    jour_distinctes = Planning.objects.values('jour').annotate(Count('id')).annotate(sort_order=preserved).order_by('sort_order')

    date_actuelle = datetime.date.today()

    if est_semaine_paire(date_actuelle):
        plannings = Planning.objects.filter(semaine__in=["0", "2"])
    else:
        plannings = Planning.objects.filter(semaine__in=["0", "1"])

    context = {
        "plannings": plannings,
        'jour_distinctes': jour_distinctes,
        'heures_distinctes': heures_distinctes
    }

    return render(request, "blog/planning.html", context)
