from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def stockproject(request):
    return render(request, 'projectdetail/stockprojectdetail.html')


def wineproject(request):
    return render(request, 'projectdetail/wineprojectdetail.html')


def visulaize(request):
    return render(request, 'projectdetail/mladditional.html')


def jobportal(request):
    return render(request, 'projectdetail/jobportaldetail.html')


def livetradeproject(request):
    return render(request, 'projectdetail/tradeprojectdetail.html')

def todoproject(request):
    return render(request, 'projectdetail/tododetail.html')


def scrapyproject(request):
    return render(request, 'projectdetail/scrapyprojectdetail.html')


def htmlproject(request):
    return render(request, 'projectdetail/htmlprojectdetail.html')

def streamlitproject(request):
    return render(request, 'projectdetail/streamlitprojects.html')




