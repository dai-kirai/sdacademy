from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.core.urlresolvers import reverse


def results(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    c = int(request.GET['c'])

    d = b ** 2 - 4 * a * c

    return render(request, 'results.html')

# Create your views here.
