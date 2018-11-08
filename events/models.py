from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from modelcluster.fields import ParentalKey
from home.blocks import ParagraphBlock, PullQuoteBlock, GalleryBlock, ContentHighlightBlock
from django import forms
from home.models import BasePageWithHero

class EventList(Page):
    subpage_types = ['events.Event']
    copy = RichTextField(null=True, blank=True, help_text="Summary to display at top of list page")

    content_panels = Page.content_panels + [
        FieldPanel('copy')
    ]

    def get_context(self, request):
        context = super(EventList, self).get_context(request)
        context['ordered_children'] = self.get_children().specific().order_by('event__start_date')
        return context

class Event(BasePageWithHero):
    start_date = models.DateField("Event start date")
    end_date = models.DateField("Event end date", null=True, blank=True)

    location = models.CharField(max_length=100)
    summary = models.CharField(max_length=600, help_text="Summary for list view, not displayed in detail view")
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField([
        ('paragraph_block', ParagraphBlock()),
        ('pull_quote_block', PullQuoteBlock()),
        ('gallery_block', GalleryBlock(ImageChooserBlock())),
        ('content_highlight_block', ContentHighlightBlock()),
    ], blank=True)


    def get_context(self, request):
        context = super(Event, self).get_context(request)
        context['subtitle'] = '{}, {}'.format(self.location, self.start_date.strftime('%b %d, %Y'))
        return context

    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('start_date', classname='full'),
        FieldPanel('end_date', classname='full'),
        FieldPanel('location', classname='full'),
        FieldPanel('summary', widget=forms.Textarea),
        ImageChooserPanel('featured_image'),
        StreamFieldPanel('body', classname='full'),
        InlinePanel('event_talks', label="Event Featured Talks"),
    ]

    parent_page_types = ['events.EventList']

class EventFeaturedTalk(Orderable, models.Model):
    talk = models.ForeignKey('talks.Talk', related_name='+', on_delete=models.CASCADE)
    event = ParentalKey('events.Event', related_name='event_talks')

    panels = [
        FieldPanel('talk')
    ]
