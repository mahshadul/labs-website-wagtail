from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import BasePageWithHero, BasePageWithBody


class ProjectList(Page):
    subpage_types = ['projects.ProjectPage']

class ProjectPage(BasePageWithHero, BasePageWithBody):

    summary = RichTextField(blank=True)

    excerpt_header = models.CharField(max_length=200, blank=True)
    excerpt = RichTextField(help_text="Summary for list view, not displayed in detail view", null=True)
    excerpt_graphic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    graphic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('summary'),
        MultiFieldPanel(
            [
                FieldPanel('excerpt_header'),
                FieldPanel('excerpt'),
                ImageChooserPanel('excerpt_graphic'),
            ],
            heading="Excerpt to display at top of page",
            classname="collapsible",
        ),
        ImageChooserPanel('graphic'),
    ] + BasePageWithBody.content_panels 

    parent_page_types = ['projects.ProjectList']
