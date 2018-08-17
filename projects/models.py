from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

from home.models import BasePageWithHero, BasePageWithBody


class ProjectList(Page):
    subpage_types = ['projects.ProjectPage']

class ProjectPage(BasePageWithHero, BasePageWithBody):

    subtitle = models.CharField(max_length=200, blank=True)
    exerpt = RichTextField(help_text="Summary for list view, not displayed in detail view")
    
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('exerpt'),
    ]

    parent_page_types = ['projects.ProjectList']
