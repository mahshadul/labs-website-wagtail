from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from home.models import BasePageWithHero

class EventList(Page):
    subpage_types = ['events.Event']

class Event(BasePageWithHero):
    date = models.DateField("Event date")
    location = models.CharField(max_length=100)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    keynotes = RichTextField(blank=True, null=True)
    event_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_context(self, request):
        context = super(Event, self).get_context(request)
        context['subtitle'] = '{} {}'.format(self.location, self.date.strftime('%b %d, %Y'))
        return context

    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('date', classname='full'),
        FieldPanel('location', classname='full'),
        StreamFieldPanel('body'),
        FieldPanel('keynotes', classname='full'),
        ImageChooserPanel('event_image'),
    ]

    parent_page_types = ['events.EventList']
