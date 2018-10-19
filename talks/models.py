from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from home.blocks import ParagraphBlock, PullQuoteBlock, GalleryBlock, ContentHighlightBlock
from wagtail.images.blocks import ImageChooserBlock

from home.models import BasePageWithHero

class TalkList(Page):
    subpage_types = ['talks.Talk']
    copy = RichTextField(null=True, blank=True, help_text="Summary to display at top of list page")

    content_panels = Page.content_panels + [
        FieldPanel('copy')
    ]


class Talk(BasePageWithHero):
    
    author = models.CharField(max_length=200)
    video_id = models.CharField(max_length=50)
    summary = RichTextField(help_text="Summary for list view, not displayed in detail view")
    date = models.DateField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=100)
    body = StreamField([
        ('paragraph_block', ParagraphBlock()),
        ('pull_quote_block', PullQuoteBlock()),
        ('gallery_block', GalleryBlock(ImageChooserBlock())),
        ('content_highlight_block', ContentHighlightBlock()),
    ], blank=True)

    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('author', classname='full'),
        FieldPanel('video_id', classname='full'),
        FieldPanel('summary', classname='full'),
        FieldPanel('date', classname='full'),
        FieldPanel('location', classname='full'),
        StreamFieldPanel('body', classname='full'),
    ]

    parent_page_types = ['talks.TalkList']
