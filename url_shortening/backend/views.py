from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import backend.models as models


def redirect_original(request, short_link):
    url = get_object_or_404(models.Link, short_link=short_link)
    url.clicked()
    return HttpResponseRedirect(url.long_link)