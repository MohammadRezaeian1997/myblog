from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article, Comment


def article_list(request):
    articles = Article.objects.all()
    data = [{'id': article.id, 'title': article.title, 'topic': article.topic} for article in articles]
    return JsonResponse(data, safe=False)


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = [{'id': comment.id, 'text': comment.text} for comment in article.comments.all()]
    data = {'id': article.id, 'title': article.title, 'content': article.content, 'topic': article.topic,
            'comments': comments}
    return JsonResponse(data)


def filter_by_topic(request, topic):
    articles = Article.objects.filter(topic=topic)
    data = [{'id': article.id, 'title': article.title, 'topic': article.topic} for article in articles]
    return JsonResponse(data, safe=False)


def add_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_id)
        text = request.POST.get('text')
        if text:
            comment = Comment(article=article, text=text)
            comment.save()
            return JsonResponse({'message': 'Comment added successfully'})
        else:
            return JsonResponse({'error': 'Comment text is required'}, status=400)
