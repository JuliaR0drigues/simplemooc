from django.shortcuts import render

def home(request):
    pagina_inicial = {}
    return render(request, 'home.html', pagina_inicial)

def contact(request):
    pagina_contato = {}
    return render(request, 'contact.html', pagina_contato)