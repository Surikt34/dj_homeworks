import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse
from _datetime import datetime
import pytz
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(timezone).strftime("%H:%M:%S")
    msg = f'Текущее московское время: {current_time}'
    return HttpResponse(msg)



def workdir_view(request):
    # Получаем текущую рабочую директорию
    workdir_path = os.getcwd()
    # Получаем список файлов и директорий
    files = os.listdir(workdir_path)

    # Создаем список файлов в виде HTML ссылок на каждый файл
    file_list = "<ul>"
    for file in files:
        file_list += f"<li>{file}</li>"
    file_list += "</ul>"

    # Ссылка на статью Википедии
    wikipedia_link = '<a href="https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9_%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3" target="_blank">Что такое рабочий каталог?</a>'

    # Формируем HTML для отображения
    msg = f"Содержимое рабочей директории:<br>{file_list}<br>{wikipedia_link}"

    return HttpResponse(msg)

