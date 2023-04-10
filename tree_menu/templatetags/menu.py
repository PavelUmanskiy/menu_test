from django import template
from django.db.models import Q

from tree_menu.models import *


register = template.Library()

symbols = "├ ─ │ └"


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, name):
    names_list = context['url_cursor'].split('/')  # Создаём "маршрут" по дереву
    for _ in range(names_list.count('')):  # Удаляем шлак в виде пустых строк
        names_list.remove('')

    if name == 'main_menu':
        nodes = list(Node.objects.select_related('parent').filter(Q(name=name) | Q(name__in=names_list) | Q(parent__name__in=names_list)))
    else:
        nodes = list(Node.objects.select_related('parent').filter(Q(name=name) | Q(parent__name=name)))
        
    return_value = {
        'nodes': nodes,
        'context': context,
        'names_list': names_list,
        'menu_name': name,
        'menu_to_display': None
    }
    return return_value