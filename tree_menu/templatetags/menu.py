from django import template
from tree_menu.models import *


register = template.Library()

symbols = "├ ─ │ └"


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(name):
    menu = list(Menu.objects.filter(name=name).select_related('node'))
    print(menu)
    return {'menu_list': menu}