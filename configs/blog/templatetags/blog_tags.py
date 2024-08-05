from django import template
from blog.models import *

register = template.Library()


@register.simple_tag()
def get_sorters():
    sorters = {
        '-views': 'Ko`rganlar ⬆',
        'views': 'Ko`rganlar ⬇',
        '-title': 'Z - A',
        'title': 'A - Z',
        '-created_at': 'Yangilari',
        'created_at': 'Eskilari'
    }
    return sorters
