from django.shortcuts import render
from .models import News, Events, Location, Contact
from .forms import ContactForm
import random
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

def home(request):
    news = News.objects.all()
    return render(request, 'index.html',{'news':news})

def search(request):
    if request.method == "POST":
        searched = request.POST['s']
        blog_result = News.objects.filter(title__contains=searched)
        event_result = Events.objects.filter(viloyat__contains=searched)
        return render(request, 'search.html',{'searched':searched, 'blog_result':blog_result,'event_result':event_result})  
    else:
        return render(request, 'search.html',{})


def requirements(request):
    return render(request, 'courses.html')

def events(request):
    locations = Location.objects.all()
    events = Events.objects.all()
    return render(request, 'events.html',{'events':events,'locations':locations})

def news(request):
    blogs = News.objects.all()
    return render(request,'news.html',{'blogs':blogs})

# def contact(request):
#     number = random.randint(1234567890, 1234567890123456789)
#     saved = False
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/contact?saved={number}')

#     else:
#         form = ContactForm
#         if f'saved{number}' in request.GET:
#             saved = True
#     return render(request,'contact.html',{'saved':saved,'form':form})

def details(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'course-single.html',{'news':news})

class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ('name','address','city','phone','image')