from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Inicio
def index(request):
    return render(request, 'app/index.html')

def detail(request, post_id):
    # Implemente a lógica para recuperar os detalhes do post
    return render(request, 'app/detail.html')


# Versão 1: Apenas com views funcionais, sem utilizar Django forms e sem validação de dados
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        # Implemente a lógica de criação de um novo post
        return redirect('post_list')
    return render(request, 'app/post_form.html')

def post_edit(request, pk):
    if request.method == 'POST':
        # Implemente a lógica de edição de um post existente
        return redirect('post_list')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_form.html', {'post': post})

def post_delete(request, pk):
    if request.method == 'POST':
        # Implemente a lógica de remoção de um post existente
        return redirect('post_list')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_confirm_delete.html', {'post': post})
