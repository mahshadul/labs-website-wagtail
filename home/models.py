from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.contrib.settings.registry import SettingMenuItem
from wagtail.core import hooks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import RichTextBlock
from wagtail.core.blocks import ListBlock

from .blocks import DetailBlock, FAIconLinkBlock
from home.blocks import GalleryBlock, ParagraphBlock, PullQuoteBlock
import feedparser


class BasePageWithHero(Page):
    subject = models.CharField(blank=True, max_length=250)
    alternate_title = models.CharField(blank=True, max_length=250)
    description = models.CharField(blank=True, max_length=500)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('subject'),
            FieldPanel('alternate_title'),
            FieldPanel('description'),
        ],
        heading="Hero Banner Content",
        )
    ]

    class Meta:
        abstract = True


class BasePageWithRSS(Page):
    feed_url = models.URLField(blank=True)
    number_of_posts = models.IntegerField(null=True)

    def get_context(self, request):
        context = super().get_context(request)
        if self.feed_url and self.number_of_posts:
            feed = feedparser.parse(self.feed_url)
            context['posts'] = feed.entries if len(feed.entries) <= self.number_of_posts else feed.entries[:self.number_of_posts]
        return context
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('feed_url'),
            FieldPanel('number_of_posts'),
        ],
        heading="RSS Feed"),
    ]

    class Meta:
        abstract = True


class HomePage(BasePageWithHero):
    about_us_title = models.CharField(blank=True, max_length=250)
    about_us_text = RichTextField(blank=True)

    featured = StreamField([
        ('event_featured', PageChooserBlock(target_model="events.Event")),
        ('talk_featured', PageChooserBlock(target_model="talks.Talk")),
        ('project_featured', PageChooserBlock(target_model="projects.ProjectPage")),
        ('event', PageChooserBlock(target_model="events.Event")),
        ('talk', PageChooserBlock(target_model="talks.Talk")),
        ('project', PageChooserBlock(target_model="projects.ProjectPage")),
    ],
    blank=True)

    content_panels = BasePageWithHero.content_panels + [
        MultiFieldPanel([
            FieldPanel('about_us_title'),
            FieldPanel('about_us_text')
        ],
        heading="About Us"),
        StreamFieldPanel('featured', classname="full"),
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

    