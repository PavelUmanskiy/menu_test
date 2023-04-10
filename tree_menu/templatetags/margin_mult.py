from django import template


register = template.Library()


@register.simple_tag
def margin_multiplicator(forloop_counter, decrement=None):
    return 12 * forloop_counter if decrement is None else 12 * forloop_counter - decrement