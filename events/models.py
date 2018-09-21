from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from modelcluster.fields import ParentalKey

from home.models import BasePageWithHero

class EventList(Page):
    subpage_types = ['events.Event']

class Event(BasePageWithHero):
    start_date = models.DateField("Event start date")
    end_date = models.DateField("Event end date", null=True)

    location = models.CharField(max_length=100)
    exerpt = RichTextField(help_text="Summary for list view, not displayed in detail view")
    event_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    def get_context(self, request):
        context = super(Event, self).get_context(request)
        context['subtitle'] = '{}, {}'.format(self.location, self.start_date.strftime('%b %d, %Y'))
        return context

    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('start_date', classname='full'),
        FieldPanel('end_date', classname='full'),
        FieldPanel('location', classname='full'),
        FieldPanel('exerpt'),
        ImageChooserPanel('event_image'),
        InlinePanel('event_talks', label="Event Featured Talks"),
    ]

    parent_page_types = ['events.EventList']

class EventFeaturedTalk(Orderable, models.Model):
    talk = models.ForeignKey('talks.Talk', related_name='+', on_delete=models.CASCADE)
    event = ParentalKey('events.Event', related_name='event_talks')

    panels = [
        FieldPanel('talk')
    ]
