from django.shortcuts import render, redirect
from contact.models import Contact
from contact.forms import ContactForm
# Create your views here.


def create(request):
    if request.method == 'POST': 
        form = ContactForm(data=request.POST) 
        context = {'form': form }
        
        # validação se o form é valido para depois conseguirmos guardar os dados adicionados na bd 
        #   vai verificar se o formulário não tem nenhum dos erros que criamos 
        if form.is_valid(): 
            print ('form is valid')
            form.save() # salvamos assim na base de dados 
            # podemos fazer também assim se quisermos alterar alguma coisa 
            # contact = form.save(commit=False)
            # contact.show = False 
            # contact.save()
            #para sairmos da pagina da criação do contacto com os dados lá, voltamos para a pagina de criação mas sem os dados 
            return redirect('contact:create')
            
        return render(request, 
                  'contact/create.html',
                  context
                  )
        
        
    context = {'form': ContactForm()}
    return render(request, 
                  'contact/create.html',
                  context
                  )