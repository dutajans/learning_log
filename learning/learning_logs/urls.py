from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),                           # Bütün konuların sayfası
    path('topics/<int:topic_id>/', views.topic, name='topic'),              # Konuların ayrı sayfaları
    path('new_topic/',views.new_topic, name='new_topic'),                   # Yeni Konu Eklemek için
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')    # Yeni Konu Eklemek için
]