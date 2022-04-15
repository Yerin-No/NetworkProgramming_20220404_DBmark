from django.urls import path
from bookmark.views import BookmarkListview, BookmarkCreateView

app_name = 'bookmark'

urlpatterns = [
    path('list/', BookmarkListview.as_view(), name='list'),  # bookmark:list
    path('add/', BookmarkCreateView.as_view(), name='add'),  # bookmark:add
]
