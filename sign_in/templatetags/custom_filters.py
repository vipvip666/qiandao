from django import template

register = template.Library()

@register.filter(name='get_teacher')
def get_teacher(name, data):
    for item in data:
        if item['name'] == name:
            return item['teacher']
    return ''
