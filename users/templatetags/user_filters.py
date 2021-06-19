'''
    Docstring
'''

from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    '''
        Docstring
    '''
    return field.as_widget(attrs={'class': 'form__input'})
