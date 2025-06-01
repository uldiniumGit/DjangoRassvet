from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'})
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'rows': 4})
    )
