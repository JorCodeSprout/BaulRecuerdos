from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cartas/', views.cartas, name='cartas'),
    path('cartas/<int:pk>/', views.detalle_carta, name='detalle_carta'),
    
    path('recuerdos/', views.recuerdos, name='recuerdos'),
    path('recuerdos/<int:pk>/', views.detalle_recuerdo, name='detalle_recuerdo'),
    
    path('razones/', views.razones, name='razones'),
    
    path('cupones/', views.cupones, name='cupones'),
    path('cupones/<int:pk>/', views.detalle_cupon, name='detalle_cupon'),
    path('cupones/<int:pk>/canjear/', views.canjear_cupon, name='canjear_cupon'),

    path('login/', auth_views.LoginView.as_view(template_name='baul/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]