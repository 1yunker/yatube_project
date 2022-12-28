from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'base.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': text,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком постов
def group_list(request):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    text = 'Лев Толстой'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)


# Страница с информацией о группах проекта Yatube
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    template = 'posts/index.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)
    # return HttpResponse(f'Пост номер {slug}')
