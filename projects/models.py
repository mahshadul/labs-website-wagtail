from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from django import forms

from home.models import BasePageWithHero
from home.blocks import ParagraphBlock, PullQuoteBlock, GalleryBlock, ContentHighlightBlock


class ProjectList(Page):
    subpage_types = ['projects.ProjectPage']
    copy = RichTextField(null=True, blank=True, help_text="Summary to display at top of list page")

    content_panels = Page.content_panels + [
        FieldPanel('copy')
    ]

class ProjectPage(BasePageWithHero):

    summary = models.CharField(max_length=600)

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    body = StreamField([
        ('paragraph_block', ParagraphBlock()),
        ('pull_quote_block', PullQuoteBlock()),
        ('gallery_block', GalleryBlock(ImageChooserBlock())),
        ('content_highlight_block', ContentHighlightBlock()),
    ], blank=True)

    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('summary', widget=forms.Textarea),
        ImageChooserPanel('featured_image'),
        StreamFieldPanel('body', classname='full'),
    ]

    parent_page_types = ['projects.ProjectList']
