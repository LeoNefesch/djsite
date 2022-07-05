from django import template
from researchers.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('researchers/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}
