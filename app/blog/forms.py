from django import forms
from .models import Comment

class EmailPostForm (forms.Form):
    name = forms.CharField(max_length=25, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Tu Correo",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    to = forms.EmailField(label="Correo a quien enviar", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(required=False,
                               label="Comentario",
                               widget=forms.Textarea(attrs={'class': 'form-control'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digita tu correo'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu comentario'}),
        }
        labels = {
            'name': 'Nombre',  # Etiqueta personalizada para el campo 'name'
            'email': 'Email',  # Etiqueta personalizada para el campo 'email'
            'body': 'Comentario',  # Etiqueta personalizada para el campo 'body'
        }