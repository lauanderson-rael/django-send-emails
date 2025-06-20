from django import forms

class EmailForm(forms.Form):
    assunto = forms.CharField(max_length=200)
    mensagem = forms.CharField(widget=forms.Textarea)
    destinatarios = forms.CharField(widget=forms.Textarea, help_text="Separe os e-mails por vírgula ou linha.")
    arquivo = forms.FileField(required=False, help_text="Seu currículo em .pdf")
