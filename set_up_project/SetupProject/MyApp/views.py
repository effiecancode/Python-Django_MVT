from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from MyApp.models import Dreamreal

# Create your views here.
def hello(request):
    today = datetime.now().date()
    daysofweek = ['mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun']
    rendered_html = render(request, 'hello.html', {'today' : today, 'days_of_week' : daysofweek})
    return rendered_html

def viewArticle(request, articleId):
    """ A view that display an article based on his ID"""
    text = "Displaying article number : %s" %articleId
    return HttpResponse(text)

def viewArticles(request, year, month):
    text = "Displaying articles of : %s/%s"%(year, month)
    return HttpResponse(text)
