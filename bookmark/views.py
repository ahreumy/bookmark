from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
# Create your views here.

class BookmarkList(ListView):
    model = Bookmark
    template_name = 'bookmark/list.html'

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields =['id' , 'site_name' , 'url']
    template_name = 'bookmark/bookmark_update.html'

class BookmarkCreate(CreateView):

    model = Bookmark
    fields =['id' , 'site_name' , 'url']
    template_name = 'bookmark/bookmark_create.html'

class  BookmarkDelete(DeleteView):
    model = Bookmark
    template_name = 'bookmark/bookmark_delete.html'
    success_url = '/'

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = 'bookmark/bookmark_detail.html'
