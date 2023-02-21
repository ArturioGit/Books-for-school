from django import forms
from .models import *


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Клас'
        self.fields['subject'].empty_label = 'Предмет'

    class Meta:
        model = Book
        fields = ['title', 'slug', 'description', 'group', 'subject', 'photo', 'pdf_file', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Назва'}),
            'slug': forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'URL'}),
            'description': forms.Textarea(attrs={'class': 'input_content', 'placeholder': 'Опис'}),
            'group': forms.Select(attrs={'class': 'input_group'}),
            'subject': forms.Select(attrs={'class': 'input_subject'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'input_boolean'}),
            'photo': forms.FileInput(attrs={'class': 'input_file', 'accept': '.jpg, .png, .jpeg'}),
            'pdf_file': forms.FileInput(attrs={'class': 'input_file', 'accept': '.pdf'})
        }
