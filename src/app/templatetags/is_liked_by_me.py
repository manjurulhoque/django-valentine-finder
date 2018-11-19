from django import template

from app.models import Like

register = template.Library()


@register.simple_tag(name='is_liked_by_me')
def is_liked_by_me(member, user):
    liked = Like.objects.filter(member=member, user=user)
    if liked:
        return True
    else:
        return False
