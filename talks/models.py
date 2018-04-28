from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from home.models import BasePageWithHero


class Talk(BasePageWithHero):

    # Database fields

    author = models.CharField(max_length=200)
    body = RichTextField()
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('author', classname='full'),
        FieldPanel('body', classname='full')
    ]
