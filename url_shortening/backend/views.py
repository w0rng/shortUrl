from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
import json
import backend.models as models


def redirect_original(request, short_link):
    url = get_object_or_404(models.Link, short_link=short_link)
    url.clicked()
    return HttpResponseRedirect(url.long_link)


def index(request):
    return render(request, 'index.html')


def shorten_url(request):
    url = request.POST.get("url", '')
    if url:
        b = models.Link(long_link=url)
        b.save()

        response_data = {'url': f'http://127.0.0.1:8000/{b.short_link}'}
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")