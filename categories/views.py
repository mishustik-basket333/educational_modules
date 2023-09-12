from django.shortcuts import render

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from categories.models import Category


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories/about.html'