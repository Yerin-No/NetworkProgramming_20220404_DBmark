from django.urls import path
from bookmark.views import BookmarkListview

app_name = 'bookmark'

urlpatterns = [
    path('list/', BookmarkListview.as_view(), name='list')  #bookmark:list
]
