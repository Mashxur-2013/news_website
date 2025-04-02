

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView, ListView

from .forms import ContactForm
from .models import News, Category
# Create your views here.

def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list":news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published )
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)


# def homePageView(request):
#     local_news = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]
#     local_one = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:1]
#     news_list = News.published.all().filter(status=News.Status.Published).order_by("-publish_time")[:15]
#     news = News.published.all()
#     categories = Category.objects.all()
#     context ={
#         "news_list": news_list,
#         "news":news,
#         "categories": categories,
#         "local_news": local_news,
#         "local":local_one,
#     }
#     return  render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by("-publish_time")[:15]

        context['local_one']= News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:1]
        context['local_news'] = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]
        context['maxalliy_xabarlar'] = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:5]

        context['xorij_one'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:1]
        context['xorij_news'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[1:6]
        context['xorij_xabarlar'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:5]

        context['sport_one'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:1]
        context['sport_news'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1:6]
        context['sport_xabarlar'] = News.published.all().filter(category__name="sport").order_by("-publish_time")[:5]

        context['tech_one'] = News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")[:1]
        context['tech_news'] = News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")[1:6]
        context['tech_xabarlar'] = News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")[
                                       :5]
        return context



# def contactPageView(request):
#     form = ContactForm(request.POST)
#     if request.method=="POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog'langaningiz uchun rahmat </h2>")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)




# def contactPageView(request):
#     context = {
#
#     }
#
#     return render(request, 'news/contact.html', context)
















class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }

        return render(request, 'news/contact.html',  context)

    def post(self, request):
        form = ContactForm(request.POST)
        if request.method =="POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'lnaganingiz uchun rahmat </h2>")
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)






def page404View(request):
    context = {

    }
    return render(request, 'news/404.html', context)