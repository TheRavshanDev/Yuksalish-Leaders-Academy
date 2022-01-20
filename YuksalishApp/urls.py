from django.urls import path
from . import views
from .views import ContactView


urlpatterns = [
    path('',views.home, name='home'),
    path('requirements/',views.requirements, name='requirement'),
    path('events/',views.events, name='event'),
    path('news/',views.news, name='news'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('search/',views.search, name='search'),
    path('news/details/<news_id>',views.details, name='detail')
]
