from django.contrib import admin
from .models import News, Events, Location, Contact, City

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title','date','text','author','image')
    list_display = ('title','date','author')
    list_filter = ('title','date','author')
    search_fields = ['title','author','date','text']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    fields = ('viloyat','city','address','phone','image','url')
    list_display = ('viloyat','city','phone','url')
    search_fields = ['viloyat','city','phone']

admin.site.register(Location)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name','address','city','phone','image')
    list_display = ('name','address','city','phone')
    search_fields = ['name','address','city','phone']
admin.site.register(City)

