from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


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

# Versão 2: Utilizando Django forms para operações CRUD
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/post_form.html'
    success_url = '/app/post_list/'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'app/post_form.html'
    success_url = '/app/post_list/'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'app/post_confirm_delete.html'
    success_url = '/app/post_list/'

# Versão 3: Views com as classes genéricas ListView, DetailView, CreateView, UpdateView e DeleteView;
class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'app/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'app/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')