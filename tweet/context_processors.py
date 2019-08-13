from django.shortcuts import render

from tweet.models import Messages


def is_read_messages(request):
    if not request.user.is_anonymous:
        return {'new_messages': Messages.objects.filter(is_read=False, to_user=request.user).exists(),'request': request}
    return {}
