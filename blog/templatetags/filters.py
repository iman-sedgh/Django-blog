from django import template

register = template.Library()
@register.filter
def get_formated_datetime(datetime):
    r = datetime.strftime("%d %B Of %Y at %H:%M")
    return r

