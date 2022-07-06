from django import template
from django.contrib.auth.models import User
from django.conf import settings

register = template.Library()


@register.filter
def is_bookmark_exist(obj, request):
    user = User.objects.get(username=request.user)
    link = settings.HOST_NAME + request.path
    return obj.filter(user=user, link=link).first()
