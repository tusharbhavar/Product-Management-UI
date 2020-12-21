from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm
from .models import Categories


def index(request):
    all_categories = Categories.objects.all()
    context = {'all_categories': all_categories}
    return render(request, 'categories/index.html', context)


def detail_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

#create
def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'categories/add.html', {'form': form})

#update
def edit_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/edit.html', {'form': form})

#delete
def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('categories:index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
