from django.conf.urls import url

from blogs import views

urlpatterns = [
    url(r'^blogs/', views.list_blogs, name='list_blogs'),
    url(r'^blog/', views.create_blog, name='create_blog'),
]
