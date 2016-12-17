
### -*- coding: utf-8 -*- ###

from django.shortcuts import render, HttpResponse
from django.template import loader, Context
from django.http import Http404, HttpRequest
from django.db.models import Q
from articles.models import Article, Excursions, Houses, Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render_to_response



def main(request):
    excursion = Excursions.objects.filter(main=True).order_by("-id")[0:5]
    house = Houses.objects.filter(main=True).order_by("-id")[0:7]
    slide = Excursions.objects.filter(slide=True).order_by("-id")[0:4]
    text = Article.objects.filter(title='Лилия-2010')
    return render_to_response('index.html',
        {'excursion':excursion,
        'house':house,
        'slide':slide,
        'text':text}
    )

def excursions(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    content = Excursions.objects.filter(id=offset)
    return render_to_response(
        'test.html', 
        {'content':content}
    )


def contact(request):
    content = Article.objects.filter(title='Контакты')
    return render_to_response(
        'test.html', 
        {'content':content}
    )

def abchazia(request):
    content = Article.objects.filter(title='Об Абхазии')
    return render_to_response(
        'test.html', 
        {'content':content}
    )

def transfer(request):
    content = Article.objects.filter(title='Трансфер')
    return render_to_response(
        'test.html', 
        {'content':content}
    )

def houses(request):
    if request.GET:
        q = Q()
        q_s = Q()
        q_t = Q()
        if str('city_1') in request.GET:
            q_s |= Q(city='Цандрипш')
        if str('city_2') in request.GET:
            q_s |= Q(city='Гагра')
        if str('city_3') in request.GET:
            q_s |= Q(city='Гудаута')
        if str('city_4') in request.GET:
            q_s |= Q(city='Пицунда')
        if str('city_5') in request.GET:
            q_s |= Q(city='Новый Афон')    
        if str('city_6') in request.GET:
            q_s |= Q(city='Сухум')

        q &= q_s

        if str('sea-left') in request.GET:
            if request.GET['sea-left'] != '':
                q &= Q(sea__gte=request.GET['sea-left'])
        if str('sea-right') in request.GET:
            if request.GET['sea-right'] != '':
                q &= Q(sea__lte=request.GET['sea-right'])

        if str('money-left') in request.GET:
            if request.GET['money-left'] != '':
                q &= Q(price__gte=request.GET['money-left'])
        if str('money-right') in request.GET:
            if request.GET['money-right'] != '':
                q &= Q(price__lte=request.GET['money-right'])

        if str('type_1') in request.GET:
            q_t |= Q(house_type='Мини-отель')
        if str('type_2') in request.GET:
            q_t |= Q(house_type='Частный дом')
        if str('type_3') in request.GET:
            q_t |= Q(house_type='Квартира')
        if str('type_4') in request.GET:
            q_t |= Q(house_type='Коттедж')
        if str('type_5') in request.GET:
            q_t |= Q(house_type='Отель')

        q &= q_t

        if str('hot_w') in request.GET:
            q &= Q(hot_w=True)
        if str('lavatory') in request.GET:
            q &= Q(lavatory=True)
        if str('w_machine') in request.GET:
            q &= Q(w_machine=True)
        if str('shower') in request.GET:
            q &= Q(shower=True)
        if str('fridge') in request.GET:
            q &= Q(fridge=True)
        if str('tv') in request.GET:
            q &= Q(tv=True)
        if str('internet') in request.GET:
            q &= Q(internet=True)
        if str('conditioner') in request.GET:
            q &= Q(conditioner=True)
        if str('safe') in request.GET:
            q &= Q(safe=True)
        if str('food') in request.GET:
            q &= Q(food=True)
        if str('balcony') in request.GET:
            q &= Q(balcony=True)

        content = Houses.objects.filter(q).order_by("-id")
    else:
        content = Houses.objects.all().order_by("-id")

    paginator = Paginator(content,12)

    page = request.GET.get('page')

    try:
        sent = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sent = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sent = paginator.page(paginator.num_pages)

    return render_to_response(
        'list_h.html',
        {'houses':sent}
    )


def home(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    content = Houses.objects.filter(id=offset)
    image = Image.objects.filter(title_id=offset)
    return render_to_response(
        'home.html', 
        {'content':content,
        'images':image}
    )

def list_ex(request):
    content = Excursions.objects.all().order_by("id")

    paginator = Paginator(content,10)

    page = request.GET.get('page')

    try:
        sent = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sent = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sent = paginator.page(paginator.num_pages)


    return render_to_response(
        'list_ex.html',
        {'content':sent}
    )

def callback(request):
    send = u"Новая заявка \n"
    if str('name') in request.GET:
        if request.GET['name'] !='':
            send = send + u' Имя: ' + request.GET['name']
    if str('surname') in request.GET:
        if request.GET['surname'] !='':
            send = send + u'\n Фамилия: ' + request.GET['surname']
    if str('email') in request.GET:
        if request.GET['email'] !='':
            send = send + u'\n E-mail: ' + request.GET['email']
    if str('phone') in request.GET:
        if request.GET['phone'] !='':
            send = send + u'\n Телефон: ' + request.GET['phone']
    if str('time_from') in request.GET:
        if request.GET['time_from'] !='':
            send = send + u'\n Удобное время для звонка с: ' + request.GET['time_from']
    if str('time_to') in request.GET:
        if request.GET['time_to'] !='':
            send = send + u' до: ' + request.GET['time_to']
    if str('date_from') in request.GET:
        if request.GET['date_from'] !='':
            send = send + u'\n Дата заезда: ' + request.GET['date_from']
    if str('date_to') in request.GET:
        if request.GET['date_to'] !='':
            send = send + u'\n Дата выезда: ' + request.GET['date_to']
    if str('people') in request.GET:
        if request.GET['people'] !='':
            send = send + u'\n Взрослых: ' + request.GET['people']
    if str('child_5') in request.GET:
        if request.GET['child_5'] !='':
            send = send + u'\n Дети до 5 лет: ' + request.GET['child_5']
    if str('child_12') in request.GET:
        if request.GET['child_12'] !='':
            send = send + u'\n Дети от 5 до 12 лет: ' + request.GET['child_12']
    if str('comment') in request.GET:
        if request.GET['comment'] !='':
            send = send + u'\n Комментарии: \n ' + request.GET['comment']


    send_house = u''

    if request.GET:
        if request.GET['id'] !='undefined':
            if request.GET['id'] !='':
                quest = request.GET['id']
                line_id = quest.split(' ')
                q = Q()
                for id in line_id:
                    q |= Q(id=id)
                content = Houses.objects.filter(q)
    
                for temp in content:
                    send_house =send_house + temp.title  + '\n'

    if send_house !='':
        send = send + u'\n Выбранные квартиры: \n ' + send_house

    send_mail('Заявка на квартиры', send, 'lilia-2010@lilia-2010.ru',['lilia-2010@inbox.ru'], fail_silently=False)
    if request.GET:
        return HttpResponse("Ваша заявка принята, благодарим за проявленный интерес! В ближайшее время мы свяжемся с вами.")
    else:
        return HttpResponse("Bad")

def favorite(request):
    if request.GET:
        if str('id') in request.GET:
            quest = request.GET['id']
            line_id = quest.split(' ')
            q = Q()
            for id in line_id:
                q |= Q(id=id)
            content = Houses.objects.filter(q)
            return render_to_response(
                'favorite.html', 
                {'content':content}
            )