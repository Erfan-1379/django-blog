from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.PostListView.as_view(), name="post_list"),
    path('posts/<pk>', views.post_detail, name="post_detail"),
    path('posts/<post_id>/comment', views.post_comment, name="post_comment"),
    path('ticket', views.ticket, name="ticket"),
    path('list_information', views.list_information),
    path('search/', views.post_search, name="post_search"),

]