from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.simple_tag
def index2(indexable, page_number, loopcounter):
    page_number = int(page_number)
    loopcounter = int(loopcounter)
    j = (page_number - 1) * 6 + loopcounter
    return indexable[j]