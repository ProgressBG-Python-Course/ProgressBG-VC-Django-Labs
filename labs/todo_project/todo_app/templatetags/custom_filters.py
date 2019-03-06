from django import template

register = template.Library()

# custom filters
@register.filter
def typeof(obj):
    return type(obj)
