# custom_filters.py

from django import template

register = template.Library()

@register.filter
def total_amount(cart_items):
    total = sum(item.product.price for item in cart_items)
    return total