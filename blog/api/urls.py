from blog.api.views import *

from django.urls import path



urlpatterns = [
    path('<int:id>', api_detail_blog_view, name='detail'),
    path('<int:id>/update', api_update_blog_view, name='update'),
    path('<int:id>/delete', api_delete_blog_view, name='delete'),
    path('create', api_create_blog_view, name='create'),
]