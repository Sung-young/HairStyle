from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000
    path('page/hairstyle', views.hairstyle, name='hairstyle'),
    path('page/community', views.community_home, name='community_home'),
    path('page/new/', views.new, name='new'),
    path('page/<int:community_id>/', views.detail, name='detail'),
    path('page/create/', views.create, name='create'),
    path('page/edit/<int:community_id>/', views.edit, name='edit'),
    path('page/update/<int:community_id>/', views.update, name='update'),
    path('page/delete/<int:community_id>/', views.delete, name='delete'),
    path('page/map', views.map, name = 'map'),
    path('page/hair/hair1', views.hair1, name = 'hair1'),
    path('page/hair/hair2', views.hair2, name = 'hair2'),
    path('page/hair/hair3', views.hair3, name = 'hair3'),
    path('page/hair/hair4', views.hair4, name = 'hair4'),
    path('page/hair/hair5', views.hair5, name = 'hair5'),
    path('page/hair/hair6', views.hair6, name = 'hair6'),
]
