from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=30)
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )
