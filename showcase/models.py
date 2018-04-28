from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock

from home.models import BasePageWithHero


class ShowcasePage(BasePageWithHero):

    subtitle = models.CharField(max_length=200, blank=True)
    body = StreamField([
        ('body', RichTextBlock())
    ])
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('body', classname='full')
    ]
