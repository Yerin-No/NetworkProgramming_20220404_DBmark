from django.shortcuts import render
from django.views.generic import ListView
from bookmark.models import Bookmark

class BookmarkListview(ListView):
    model = Bookmark
    #bookmark_list.html, {'bookmark_list':Bookmark.object.all()}


