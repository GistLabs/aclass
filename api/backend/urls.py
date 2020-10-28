
# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('api/', RedirectView.as_view(url='/api/v1/')),
    path('', RedirectView.as_view(url='/api/v1/')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
