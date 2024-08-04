from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from pevnostnituristikaweb.models import Museum  # Odkazujeme přímo na model Museum
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class MuseumCreateView(CreateView):
    model = Museum  # Odkazujeme správně na model Museum
    template_name = "museums/create_museum.html"
    fields = ["name", "location", "web"]
    success_url = reverse_lazy("index")
