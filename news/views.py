from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

def index(request):
    news = News.objects.all()
    recent_news = News.objects.order_by('-created_at')[:2]
    category = Category.objects.all()
    context = {
        'news': news, 
        'recent_news': recent_news,
        'category': category,
        'title': 'News Listing',
        'address': 'MK, Mark Tven, Skopje 1000'}
    return render(request, 'news/index.html', context)
