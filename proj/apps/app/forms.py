from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

    