from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Client, News
from .forms import ContactForm
from django.core.mail import send_mail


def get_top_news_context():
    news = News.objects.order_by('-id')
    context = {}
    if len(news) > 0:
        context['news00'] = news[0]
    if len(news) > 1:
        context['news01'] = news[1]
    if len(news) > 2:
        context['news02'] = news[2]
    return context


# Главная страница
def main_view(request):
    client = Client.objects.all()
    context = {'client': client}
    context.update(get_top_news_context())
    return render(request, 'test_app/index.html', context=context)


# Цены
def show_prices(request):
    context = get_top_news_context()
    return render(request, 'test_app/pricing.html', context=context)


# Наши услуги. 4 вкладки
def delivery_to_rf(request):
    context = get_top_news_context()
    return render(request, 'test_app/DeliveryToRF.html', context=context)


def redemption_of_goods(request):
    context = get_top_news_context()
    return render(request, 'test_app/RedemptionOfGoods.html', context=context)


def goods_check(request):
    context = get_top_news_context()
    return render(request, 'test_app/GoodsCheck.html', context=context)


def export_of_personal_belongings(request):
    context = get_top_news_context()
    return render(request, 'test_app/ExportOfPersonalBelongings.html', context=context)


# TODO страница пока не используется
def about(request):
    context = get_top_news_context()
    return render(request, 'test_app/about.html', context=context)


# Оставить заявку
def application(request):
    context = get_top_news_context()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            # сохранить данные в Client
            Client.objects.create(name=name, email=email, description=message)

            send_mail(
                'contact',
                f'{name}, ваше сообщение "{message}" принято',
                'uldinium@yandex.ru',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('test_app:index'))
        else:
            context['form'] = form
            return render(request, 'test_app/application.html', context=context)
    else:
        form = ContactForm()
        context['form'] = form
        return render(request, 'test_app/application.html', context=context)


# TODO страница лишняя, надо убрать после того, как доделаю новую страницу со списком новостей
def news_list(request):
    context = get_top_news_context()
    return render(request, 'test_app/news.html', context=context)


def contact(request):
    context = get_top_news_context()
    return render(request, 'test_app/contact.html', context=context)



def news1(request):
    context = get_top_news_context()
    return render(request, 'test_app/news1.html', context=context)


def news2(request):
    context = get_top_news_context()
    return render(request, 'test_app/news2.html', context=context)


def news3(request):
    context = get_top_news_context()
    return render(request, 'test_app/news3.html', context=context)


def more_news(request):
    news = News.objects.order_by('-id')
    context = {'news': news}
    context.update(get_top_news_context())
    return render(request, 'test_app/moreNews.html', context=context)
