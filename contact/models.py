from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# id (primary key) -> gerado automaticamente pelo django
# first_name(string), last_name(string), phone(string)
# email(email), created_date(date), description(text)
# os que não têm blank são obrigatorios e na parte de admin do django aparecem a negrito para serem preenchidos 

# depois
# category(foreign key), show(boolean), owner(foreign key), 
# picture(image)
# foreign key -> vai "apontar" para outra tabela

# vamos criar a foreign key - category 
class Category(models.Model): 
    # colocar o nome que aparece no plural de outra maneira 
    class Meta: 
        verbose_name = 'Category' # singular 
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.name}'

# estamos a criar a tabela contacto
class Contact(models.Model): 
    # criar campos na tabela 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) # blank -> para ser opcional
    created_date = models.DateTimeField(default=timezone.now) # não vamos querer que seja regitado pela pessoa
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) #on_delete o que vai acontecer ao contacto quando apagarmos a categoria 
    # CASCADE -> todos os contactos daquela familia vao ser elmininados
    # SET_NULL -> vai colocar o campo category a null
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

