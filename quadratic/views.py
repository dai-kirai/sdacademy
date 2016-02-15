from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.core.urlresolvers import reverse


def check_int(string):
    global notint
    try:
        return int(string)
    except ValueError:
        notint = True


def quadratic_results(request):
    global notint
    notint = False
    x1 = 0
    x2 = 0
    a = request.GET.get(u'a', '')
    b = request.GET.get(u'b', '')
    c = request.GET.get(u'c', '')

    a1 = check_int(a)
    b1 = check_int(b)
    c1 = check_int(c)

    context = {'a': a, 'b': b, 'c': c, 'a1': a1, 'b1': b1, 'c1': c1, 'notint': notint}

    if not notint and (a1 != 0):
        d = b1 ** 2 - 4 * a1 * c1
        if d >= 0:
            x1 = (-b1 - d ** (1/2.0)) / (2 * a1)
            x2 = (-b1 + d ** (1/2.0)) / (2 * a1)
        context.update({'d': d, 'x1': x1, 'x2': x2})

    return render(request, 'results.html', context)


# Create your views here.
