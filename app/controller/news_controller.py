from app.model.models import News

def get_all_news(request):
    news=News.objects.all().order_by('-date')
    return news

def get_all_visible_news(request):
    news=News.objects.filter(visible=True).order_by('-date')
    return news

def get_news_by_id(request, id_news):
    news = News.objects.get(ID = id_news)
    return news

def get_last_five_news(request):
    news=News.objects.filter(visible=True).order_by('-date')[:3]
    return news