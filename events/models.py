from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from home.models import BasePageWithHero, BasePageWithBody

class EventList(Page):
    subpage_types = ['events.Event']

class Event(BasePageWithHero, BasePageWithBody):
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
        context['subtitle'] = '{}, {}'.format(self.location, self.date.strftime('%b %d, %Y'))
        return context

    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('start_date', classname='full'),
        FieldPanel('end_date', classname='full'),
        FieldPanel('location', classname='full'),
        FieldPanel('exerpt'),
        ImageChooserPanel('event_image'),
    ]

    parent_page_types = ['events.EventList']
