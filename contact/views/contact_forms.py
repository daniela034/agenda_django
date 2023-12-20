from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from contact.forms import ContactForm
from django.urls import reverse
# Create your views here.


def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST': 
        form = ContactForm(request.POST, request.FILES) 
        context = {'form': form , 'form_action': form_action}
        
        # validação se o form é valido para depois conseguirmos guardar os dados adicionados na bd 
        #   vai verificar se o formulário não tem nenhum dos erros que criamos 
        if form.is_valid(): 
            print ('form is valid')
            contact = form.save() # salvamos assim na base de dados 
            # podemos fazer também assim se quisermos alterar alguma coisa 
            # contact = form.save(commit=False)
            # contact.show = False 
            # contact.save()
            #para sairmos da pagina da criação do contacto com os dados lá, voltamos para a pagina de criação mas sem os dados 
            return redirect('contact:update', contact_id=contact.pk )
            
        return render(request, 
                  'contact/create.html',
                  context
                  )
        
        
    context = {'form': ContactForm(), 'form_action': form_action}
    return render(request, 
                  'contact/create.html',
                  context
                  )
    

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST': 
        form = ContactForm(request.POST, request.FILES, instance=contact) 
        context = {'form': form , 'form_action': form_action}
        
        if form.is_valid(): 
            print ('form is valid')
            contact = form.save() # salvamos assim na base de dados 
            return redirect('contact:update', contact_id=contact.pk )
            
        return render(request, 
                  'contact/create.html',
                  context
                  )
        
        
    context = {'form': ContactForm(instance=contact), 'form_action' : form_action}
    return render(request, 
                  'contact/create.html',
                  context
                  )
    
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes': 
        contact.delete()
        return redirect('contact:index')
    
    return render(request, 'contact/contact.html', context={'contact':contact, 'confirmation' : confirmation})