from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Livro

def index(request):
    livros_list = Livro.objects.order_by('-pub_date')[:5]
    template = loader.get_template('locacao/index.html')
    context = {
        'livros_list': livros_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, livro_id):
    try:
        livro = Livro.objects.get(pk=livro_id)
    except Livro.DoesNotExist:
        raise Http404("Livro não existe")
    return render(request, 'locacao/view.html', {'livro': livro})