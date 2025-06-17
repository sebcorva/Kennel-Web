from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Filtro para acceder a elementos de un diccionario en plantillas"""
    return dictionary.get(key) 