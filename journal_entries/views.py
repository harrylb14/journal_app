from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Resource


class IndexView(generic.ListView):
    template_name = 'journal_entries/index.html'
    context_object_name = 'resource_list'

    def get_queryset(self):
        return Resource.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Resource
    template_name = 'journal_entries/detail.html'
