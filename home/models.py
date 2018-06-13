from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.contrib.settings.registry import SettingMenuItem
from wagtail.core import hooks
from .blocks import DetailBlock, HeroBlock, FAIconLinkBlock, RSSBlock


class BasePageWithHero(Page):
    banner = StreamField([
        ('banner', HeroBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('banner')
    ]

    class Meta:
        abstract = True


class HomePage(BasePageWithHero):
    about_us = StreamField([
        ('about_us', DetailBlock())
    ])

    featured = StreamField([
        ('event_featured', PageChooserBlock(target_model="events.Event")),
        ('talk_featured', PageChooserBlock(target_model="talks.Talk")),
        ('showcase_featured', PageChooserBlock(target_model="showcase.ShowcasePage")),
        ('event', PageChooserBlock(target_model="events.Event")),
        ('talk', PageChooserBlock(target_model="talks.Talk")),
        ('showcase', PageChooserBlock(target_model="showcase.ShowcasePage")),
    ])

    rss_feed = StreamField([
        ('rss_feed', RSSBlock()),
    ], blank=True)

    content_panels = BasePageWithHero.content_panels + [
        StreamFieldPanel('about_us', classname="full"),
        StreamFieldPanel('featured', classname="full"),
        StreamFieldPanel('rss_feed')
    ]

@register_setting(icon="list-ul")
class NavLinks(BaseSetting):
    links = StreamField([
        ('pages', PageChooserBlock()),
        ('icons', FAIconLinkBlock()),
    ])

    panels = [
        StreamFieldPanel('links')
    ]

@hooks.register('register_admin_menu_item')
def register_navlinks_menu_item():
    '''
    Generate a second menu button at the root of the Admin sidebar
    '''
    return SettingMenuItem(NavLinks, icon="list-ul")
