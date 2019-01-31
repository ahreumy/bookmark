from django.urls import path

from .views import BookmarkList,BookmarkUpdate,BookmarkCreate,BookmarkDelete,BookmarkDetail
urlpatterns = [
    path('',BookmarkList.as_view(),name='bookmark_list'),
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name='bookmark_update'),
    path('create/', BookmarkCreate.as_view(), name='bookmark_create'),
    path('delete/<int:pk>/', BookmarkDelete.as_view(), name='bookmark_delete'),
    path('detail/<int:pk>/',BookmarkDetail.as_view(), name='bookmark_detail'),

]