from django.urls import path
from a_post import views


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('<slug:slug>/', views.post_detail, name='post-detail'),
]