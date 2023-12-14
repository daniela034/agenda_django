from django.contrib import admin
#from .models import Contact -> uma forma de importar
from contact import models 
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin): 
    list_display = ('id','first_name', 'last_name', 'phone','created_date',) 
    ordering = '-id', 
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name' 
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', # para conseguirmos editar sem ir ao contacto
    list_display_links = 'id', 'phone', # onde vamos ter o link para o contacto

# register Category model 
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('id','name',) 