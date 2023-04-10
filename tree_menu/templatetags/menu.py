from django import template
from django.db.models import Q

from tree_menu.models import *


register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, name):
    names_list = context['url_cursor'].split('/')  # Создаём "маршрут" по дереву
    for _ in range(names_list.count('')):  # Удаляем шлак в виде пустых строк
        names_list.remove('')

    nodes = Node.objects.select_related('parent').filter(Q(name=name) | Q(related_menu__name=name))
        
    return_value = {
        'nodes': nodes,
        'context': context,
        'names_list': names_list,
        'menu_name': name,
    }
    return return_value


