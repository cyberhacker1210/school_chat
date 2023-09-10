from django import template

register = template.Library()

@register.simple_tag
def get_planning(plannings, heure, jour):
    for planning in plannings:
        if planning.heure == heure and planning.jour == jour:
            return planning.matiere
    return ''

