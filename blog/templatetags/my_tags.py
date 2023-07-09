from django import template

register = template.Library()

# Создание тега
#@register.simple_tag

@register.simple_tag
@register.filter()
def mediapath(val) -> str:
    return f'/media/{val}' if val else '/media/Template_image.png'