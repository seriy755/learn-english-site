"""learn_english_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vocabulary', views.vocabulary),
    path('educational-materials', views.education_materials),
    path('cards', views.cards),
    path('word-add', views.word_add),
    path('send-word', views.send_word),
    path('word-edit/<int:pk>', views.word_edit),
    path('cards/<int:current>', views.cards),
    path('material-add', views.material_add),
    path('send-material', views.send_material),
]
