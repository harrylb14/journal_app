from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django_tables2 import RequestConfig

from .forms import ResourceForm
import django_tables2 as tables

from .models import Resource, Language, Framework
from .tables import ResourceTable


class IndexView(tables.SingleTableView):
    template_name = 'journal_entries/index.html'
    model = Resource

    def get_queryset(self):
        return Resource.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        form = ResourceForm()
        table = ResourceTable(self.get_queryset())

        context['form'] = form
        context['table'] = table

        return context

    def post(self, request):
        form = ResourceForm(data=request.POST)
        if form.is_valid():

            new_resource = form.save(commit=False)
            new_resource.pub_date = timezone.now()
            new_resource.save()

        return HttpResponseRedirect(reverse('journal_entries:index'))


def create_resource_ajax(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
    else:
        form = ResourceForm()

    return save_resource_form(request, form, 'journal_entries/partial_resource_create.html')


def update_resource_ajax(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
    else:
        form = ResourceForm(instance=resource)

    return save_resource_form(request, form, 'journal_entries/partial_resource_update.html')


def delete_resource_ajax(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    data = dict()
    if request.method == 'POST':
        resource.delete()
        data['form_is_valid'] = True
        resource_list = Resource.objects.order_by('-pub_date')
        data['html_resource_list'] = ResourceTable(resource_list).as_html(request)
    else:
        context = {'resource': resource}
        data['html_form'] = render_to_string('journal_entries/partial_resource_delete.html',
                                             context,
                                             request=request,
                                             )

    return JsonResponse(data)


def save_resource_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():

            new_resource = form.save(commit=False)

            if new_resource.pub_date is None:
                new_resource.pub_date = timezone.now()
            new_resource.save()

            languages = list(form.cleaned_data['language'])
            frameworks = list(form.cleaned_data['framework'])

            for language in languages:
                new_resource.languages.add(language)

            for framework in frameworks:
                new_resource.frameworks.add(framework)

            data['form_is_valid'] = True
            resource_list = Resource.objects.order_by('-pub_date')
            data['html_resource_list'] = ResourceTable(resource_list).as_html(request)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request,
                                         )

    return JsonResponse(data)


def ajax_search(request):
    data = {}
    search_term = request.GET['search'].strip()
    search_class = request.GET['class'].strip()
    if search_class == 'language':
        language = Language.objects.get(tag=search_term)
        resource_list = language.resource_set.all().order_by('-pub_date')
    elif search_class == 'framework':
        framework = Framework.objects.get(tag=search_term)
        resource_list = framework.resource_set.all().order_by('-pub_date')
    else:
        resource_list = Resource.objects.all().order_by('-pub_date')

    data['html_resource_list'] = ResourceTable(resource_list).as_html(request)

    return JsonResponse(data)

