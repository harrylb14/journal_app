import django_tables2 as tables
from django_tables2 import TemplateColumn
from django.utils.html import format_html
from .models import Resource


class ResourceTable(tables.Table):
    class Meta:
        model = Resource
        template_name = "django_tables2/bootstrap4.html"
        sequence = ('title', 'languages', 'frameworks', 'pub_date')
        exclude = ('id', 'description', 'link')
        attrs = {'id': 'resource_list'}
        orderable = False

    def render_title(self, record, value):
        resource_title = value
        resource_link = record.link
        return format_html(f"<a href='{resource_link}' id='resource_title'>  {resource_title} </a>")

    def render_pub_date(self, value):
        return value.strftime('%d %b %y')

    def render_languages(self, value):
        html = ""
        for language in value:
            url = 'ajax_search/'
            html += f"<a class='language' id={language.lower()} href={url}> {language} </a>"

        return format_html(html)

    def render_frameworks(self, value):
        html = ""
        for framework in value:
            url = 'ajax_search/'
            html += f"<a class='framework' id={framework.lower()} href={url}> {framework} </a>"

        return format_html(html)

    languages = tables.Column(accessor='all_languages')
    frameworks = tables.Column(accessor='all_frameworks')
    edit = TemplateColumn(template_name='journal_entries/edit_button.html', verbose_name='')
    delete = TemplateColumn(template_name='journal_entries/delete_button.html', verbose_name='')
