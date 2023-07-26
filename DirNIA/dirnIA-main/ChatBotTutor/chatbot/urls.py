from django.urls import path

from . import views

urlpatterns = [
    path('', views.initialize, name='initialize'),
    path('get_text/<str:message>', views.get_text, name='get_text'),
    path('get_materials', views.get_materials, name='get_materials'),
    path('index', views.index, name='index')
]