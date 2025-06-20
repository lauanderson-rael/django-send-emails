from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
   if (request.method == 'POST'):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('enviar_email')
      else:
         login_form = AuthenticationForm() # retorna form vazio na tela
   else:
      login_form = AuthenticationForm()
   return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
   logout(request)
   return redirect('login')