from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import Categories
from .forms import CategoryForm

def index(request):
    all_categories = Categories.objects.all()    #retrive all categories
    context = {'all_categories': all_categories}
    return render(request, 'categories/index.html', context)


def detail_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)   #retrive single category
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

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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