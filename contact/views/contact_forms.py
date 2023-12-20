from django.shortcuts import get_object_or_404,render, redirect
from contact.models import Contact
from django.db.models import Q # para fazer o ou na query 
from django.core.paginator import Paginator # forma de criar paginas para os contactos 
# Create your views here.
def create(request): 
    context = {}
    return render(request, 
                  'contact/create.html',
                  context
                  )