from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    # return HttpResponse('Oi')
    return render(req, 'index.html')