from django import forms

from app.models import Animal


class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form'

    class Meta:
        model = Animal
        fields = '__all__'
