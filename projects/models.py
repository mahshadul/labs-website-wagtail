from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import BasePageWithHero, BasePageWithBody


class ProjectList(Page):
    subpage_types = ['projects.ProjectPage']

class ProjectPage(BasePageWithHero, BasePageWithBody):

    subtitle = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    exerpt = RichTextField(help_text="Summary for list view, not displayed in detail view")
    date = models.DateField()

    graphic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        FieldPanel('exerpt'),
        FieldPanel('date'),
        ImageChooserPanel('graphic'),
    ]

    parent_page_types = ['projects.ProjectList']
