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

class ContactsView(TemplateView):
    template_name = 'contacts.html'
