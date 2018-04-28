from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import StructBlock, CharBlock, PageChooserBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
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

    talk_page = models.ForeignKey(
        'talks.Talk',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    event_page = models.ForeignKey(
        'events.Event',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    content_panels = BasePageWithHero.content_panels + [
        StreamFieldPanel('about_us', classname="full"),
        PageChooserPanel('talk_page', 'talks.Talk'),
        PageChooserPanel('event_page', 'events.Event')
    ]