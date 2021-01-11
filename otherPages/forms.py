from django import forms
from django.utils.translation import get_language


class ContactEmailForm(forms.Form):
    from_email = forms.CharField(label='E-mail')
    email_message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactEmailForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            current_language = get_language()
            if field_name == 'from_email':
                if current_language == 'es':
                    field.widget.attrs['placeholder'] = 'Correo electronico'
                else:    
                    field.widget.attrs['placeholder'] = 'E-mail'
            if field_name == 'email_message':
                if current_language == 'es':
                    field.widget.attrs['placeholder'] = 'Nombre + Mensaje'
                elif current_language == 'en':
                    field.widget.attrs['placeholder'] = 'Name + Message'
                else:
                    field.widget.attrs['placeholder'] = 'Nome + Mensagem'
                field.widget.attrs['rows'] = '3'
        