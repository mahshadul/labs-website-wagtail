from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class HomePage(Page):
    about_us = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('about_us', classname="full"),
    ]

class HeroBlock(StructBlock):
    subject = CharBlock()
    byline = CharBlock(required=False)

    class Meta:
        icon = "user"
        template = "home/blocks/hero.html"

class BasePageWithHero(Page):
    hero = StreamField([
        ('hero', HeroBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('hero')
    ]

    class Meta:
        abstract = True
