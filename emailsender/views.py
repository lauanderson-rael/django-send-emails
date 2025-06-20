
from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import EmailMessage
import time

def enviar_email(request):
    #if not request.user.is_authenticated:
       # return redirect('login')

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            destinatarios_raw = form.cleaned_data['destinatarios']
            arquivo = request.FILES.get('arquivo')

            lista_emails = [email.strip() for email in destinatarios_raw.replace('\n', ',').split(',') if email.strip()]

            for email_destino in lista_emails:
                email = EmailMessage(
                    assunto,
                    mensagem,
                    'lauanderson38@gmail.com',
                    [email_destino]
                )
                if arquivo:
                    email.attach(arquivo.name, arquivo.read(), 'application/pdf')
                email.send()
                time.sleep(3)

            return render(request, 'email_sucesso.html')
    else:
        form = EmailForm()

    return render(request, 'enviar_email.html', {'form': form})
