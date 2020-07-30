from app.model.models import News

def get_all_news(request):
    news=News.objects.all()
    return news