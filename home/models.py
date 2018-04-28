from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from .blocks import DetailBlock, HeroBlock


class BasePageWithHero(Page):
    hero = StreamField([
        ('hero', HeroBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('hero')
    ]

    class Meta:
        abstract = True

        
class HomePage(BasePageWithHero):
    about_us = StreamField([
        ('about_us', DetailBlock())
    ])

    content_panels = BasePageWithHero.content_panels + [
        StreamFieldPanel('about_us', classname="full"),
    ]