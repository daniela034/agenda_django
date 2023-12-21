from django.contrib import admin 
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name ='search'),
    path('', views.index, name='index'), 
    
    # quando são paginas dinâmicas por exemplo para o contacto 
    # usamos o CRUD
    path('contact/<int:contact_id>/', views.contact, name='contact'), # leitura
    path('contact/create/', views.create, name='create'), 
    path('contact/<int:contact_id>/update/', views.update, name='update'), # update do contacto 
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # update do contacto 

    # user
    path('user/create/', views.register, name='register'), 
    path('user/login/', views.login_view, name='login'), 
    path('user/logout/', views.logout_view, name='logout'),  # type: ignore

]
