from django import template

register = template.Library()

@register.filter
def star_rating(value):
    try:
        return '⭐️' * int(value)
    except (ValueError, TypeError):
        return ''
