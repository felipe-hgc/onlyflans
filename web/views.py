from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from web.forms import ContactFormForm, ContactFormModelForm
from web.models import Flan, ContactForm



def indice(request):
    flanes = Flan.objects.filter(is_private=False)
    diccionario = {'flanes': flanes}
    return render(request, 'index.html', diccionario)


def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenido(request):
    flanes = Flan.objects.filter(is_private=True)
    if request.user.groups.filter(name__in='1').exists():
        diccionario = {'flanes': flanes, 'saludo':'Bienvenida'}
    else:
        diccionario = {'flanes': flanes, 'saludo':'Bienvenido'}
    return render(request, 'welcome.html', diccionario)

@login_required
def catalogo(request):
    flanes = Flan.objects.all().order_by('-is_new').values()
    diccionario = {'flanes': flanes}
    return render(request, 'catalogo.html', diccionario)


def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        # form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # form.save()
            return HttpResponseRedirect('/exito/')

    else:
        form = ContactFormForm()
        # form = ContactFormModelForm()

    return render(request, 'contacto.html', {'form': form})


def exito(request):
    return render(request, 'exito.html')
