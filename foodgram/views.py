from django.shortcuts import render


def error404(request, exception):
    text = '404. Страница которую вы ищете не найдена.'
    caption = '404'
    return render(request, 'errorPage.html',
                  {'text': text, 'caption': caption}, status=404)


def error500(request):
    text = '500. Мы не смогли обработать ваш запрос.'
    caption = '500'
    return render(request, 'errorPage.html',
                  {'text': text, 'caption': caption}, status=500)
