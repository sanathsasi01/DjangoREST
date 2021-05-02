from blog.api.views import api_detail_blog_view

from django.urls import path



urlpatterns = [
    path('<int:id>', api_detail_blog_view, name='detail')
]