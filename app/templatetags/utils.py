from django import template

register = template.Library()

@register.filter(name="div")
def div(value, args):
    return (value / args *100)