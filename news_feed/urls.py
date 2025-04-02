from django.urls import path
from .views import (
    news_list,
    news_detail,
    # homePageView,
    # contactPageView,
    ContactPageView,
    page404View,
    HomePageView

)


urlpatterns = [
    # path('', homePageView, name="home_page" ),
    path('', HomePageView.as_view(), name='home_page'),
    path('news/all/', news_list, name = "all_news_list"),
    path("news/<slug:news>/", news_detail, name = "news_detail_page"),
    # path("contact-us/", contactPageView, name="contact_page"),
    path("contact_us", ContactPageView.as_view(), name="contact_page"),
    path("404/", page404View, name='404_page')

]
