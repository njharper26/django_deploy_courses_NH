from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'delete/(\d+)', views.delete),
    url(r'destroy/(\d+)', views.destroy),
    url(r'create', views.update)
]