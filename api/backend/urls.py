
# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('', RedirectView.as_view(url='/api')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
