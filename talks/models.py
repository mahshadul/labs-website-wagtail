from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from home.models import BasePageWithHero


class TalkList(Page):
    subpage_types = ['talks.Talk']


class Talk(BasePageWithHero):

    # Database fields

    author = models.CharField(max_length=200)
    video_id = models.CharField(max_length=50)
    exerpt = RichTextField(help_text="Summary for list view, not displayed in detail view")
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('author', classname='full'),
        FieldPanel('video_id', classname='full'),
        FieldPanel('exerpt', classname='full'),
        StreamFieldPanel('body', classname='full'),
    ]

    parent_page_types = ['talks.TalkList']
