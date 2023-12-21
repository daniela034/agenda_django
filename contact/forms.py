from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
    picture = forms.ImageField(
        widget=forms.FileInput(attrs={'accept':'image/*'})
    )
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        
        #self.fields['first_name'].widget.attrs.update(
        #    {'placeholder' : 'Insert your name - i'}
        #)
        
    class Meta: 
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category','picture',)
        
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
        
        
        
#usar um formulários para os utilizadores 
class RegisterForm(UserCreationForm): 
    
    # the field email is required
    email = forms.EmailField()
    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1','password2',)
        
    def clean_email(self): 
        email = self.cleaned_data.get('email')
        #verify if emails exists in db
        if User.objects.filter(email=email).exists(): 
            self.add_error('email', 
                        ValidationError('Email already exists', code='invalid')) 
        
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )
    
    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username',)
        
    def save(self, commit=True): 
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')
        if password: 
            user.set_password(password)
        if commit: 
            user.save()
        return user
    
    def clean(self): 
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2: 
                self.add_error('password2', ValidationError('Different passwords') )

        return super().clean()
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('email already exists', code='invalid')
                )

        return email
    
    def clean_password1(self): 
        password1 = self.cleaned_data.get('password1')
        
        if password1: 
            try: 
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
                    
        return password1