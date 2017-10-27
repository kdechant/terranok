from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField


class Project(Page):
    image = models.ImageField(upload_to='projects', blank=True)
    content = RichTextField(_("Content"), null=True, blank=True)
    external_url = models.URLField("External URL", null=True, blank=True)

    search_fields = ("content",)
