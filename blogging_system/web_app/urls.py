from django.urls import path

from web_app.views import index, new, create

urlpatterns = [
    path('', index, name='index'),
    path('new', new, name='new'),
    path('create', create, name='create'),
]
