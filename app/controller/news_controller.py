from app.model.models import News

def get_all_news(request):
    news=News.objects.all()
    return news

def get_news_by_id(request, id_news):
    news = News.objects.get(ID = id_news)
    return news