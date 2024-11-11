from django.shortcuts import render

def home(request):
    news = [
        {
            'title':'Назва першої статті',
            'text':'Повний текст',
            'data':'12.12.12'
        },
        {
            'title': 'Назва другої статті',
            'text': 'Повний текст',
            'data': '12.12.12'
        }
    ]
    data = {
        'news': news,
        'title': 'Головна сторінка'
    }
    return render(request, 'web/home.html', data)


def about(request):
    return render(request, 'web/about.html')
