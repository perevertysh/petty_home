from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from pets.models import Pet


class IndexPageView(TemplateView):
    template_name = 'index.html'


class PetListView(ListView):
    model = Pet


class PetCreateView(CreateView):
    model = Pet
    fields = ['name']


class PetUpdateView(UpdateView):
    model = Pet
    fields = ['name']


class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy('pet-list')
