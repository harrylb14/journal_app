from django.db import models


class Language(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Framework(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    link = models.URLField()
    languages = models.ManyToManyField(Language)
    frameworks = models.ManyToManyField(Framework)
    pub_date = models.DateTimeField('date added')

    def __str__(self):
        return self.title

    @property
    def all_languages(self):
        return [x.tag for x in self.languages.all()]

    @property
    def all_frameworks(self):
        return [x.tag for x in self.frameworks.all()]
