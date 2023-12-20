from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError

#criar um forms aqui dentro que depois vai ser movido 
# vamos usar o ModelForm porque já tem os campos (Form baseado no nosso modelo)
class ContactForm(forms.ModelForm):
    # indicar o model e os campos que queremos que sejam exibidos
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'insert your name',
            }
        ),
        label='First Name - forms',
        help_text='Help text for user',
    )
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        
        #self.fields['first_name'].widget.attrs.update(
        #    {'placeholder' : 'Insert your name - i'}
        #)
        
    class Meta: 
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category',)
        
        #widgets = {
        #    'first_name' : forms.TextInput(
        #        attrs={
        #            'placeholder' : 'Insert your name'
        #        }
        #    )
        # }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        #self.add_error('first_name', ValidationError('Mensagem de erro', code='invalid') )
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name: 
            self.add_error('last_name', ValidationError('First name can not be the same as the last name', code='invalid'))
        
        return super().clean()
    
    #validar o campo 
    def clean_first_name(self): 
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC': 
            # com o raise vai parar a execução dos erros aqui, se tivermos mais erros não nos vai apresentar
            #raise ValidationError('Não digite ABC neste campo', code='invalid')
            self.add_error('first_name', ValidationError('Mensagem de erro', code='invalid') )
        return first_name
        