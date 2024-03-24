from django import template

register = template.Library()


@register.simple_tag()
def mymedia(image):
    if image:
        return image.url
    return '#'
