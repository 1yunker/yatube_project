from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


# Create your views here.
# Главная страница
def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'base.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон

    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': text,
        'posts': posts,
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
    template = 'posts/group_list.html'
    # title = 'Здесь будет информация о группах проекта Yatube'

    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    context = {        
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
    # return HttpResponse(f'Пост номер {slug}')
