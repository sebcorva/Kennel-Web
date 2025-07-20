from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Filtro para acceder a elementos de un diccionario por clave"""
    return dictionary.get(key) 