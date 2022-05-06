from .models import Memories
from django.forms import ModelForm, TextInput, Textarea


class MemoriesForm(ModelForm):
    class Meta:
        model = Memories
        fields = ['title', 'description', 'location']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control text-field',
                'placeholder': 'Enter the title',
                'id': 'title_memory'
            }),
            'description': Textarea(attrs={
                'class': 'form-control description-field',
                'placeholder': "Enter a description",
                'id': 'description_memory'
            }),
            'location': TextInput(attrs={
                'class': 'form-control text-field',
                'id': 'location_memory',
            }),
        }
