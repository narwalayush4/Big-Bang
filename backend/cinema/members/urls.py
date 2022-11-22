from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('details/', views.index, name='moviedetails'),
    path('', views.home, name='home'),
    path('details/<int:product_id>/', views.watchlist_add, name='watchlist_add'),
    path('details/', views.getwatchlist, name='getwatchlist'),
    path('register/',views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path('search', views.searchmovie, name='searchmoviename'),

]