from django.conf.urls import url

from blogs import views

urlpatterns = [
    url(r'^blogs/', views.list_blogs),
    url(r'^blog/', views.create_blog),
]
