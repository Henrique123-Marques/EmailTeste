from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

# Create your views here.
def contato(request):
	if str(request.method) == 'POST':
		form = ContatoForm(request.POST)
		if form.is_valid():
			form.send_email()
			messages.success(request, 'Email enviado')
			form = ContatoForm()
		else:
			messages.error(request, 'Email NÃO enviado')
	else:
		form = ContatoForm()
	context = {
		"form":form
	}
	return render(request, "contato.html", context)