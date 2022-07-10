from wsgiref import headers
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from .blocks import RosterBlock
from wagtail.models import Orderable, Page
from modelcluster.fields import ParentalKey
from wagtail.core.fields import StreamField, RichTextField
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel

# social links set for global access

@register_setting
class SocialMediaSettings(BaseSetting):
    instagram = models.CharField(max_length=255, help_text='Instagram username, without the @')
    youtube = models.URLField(help_text='YouTube channel or user account URL')
    spotify = models.URLField(help_text='Spotify account or playlist URL')
    twitter = models.CharField(max_length=255, help_text='Twitter username, without the @')
    tiktok = models.CharField(max_length=255, help_text='TikTok username, without the @')

# contact form

class FormField(AbstractFormField):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='form_fields')


# social images with links

class SocialImages(Orderable):
    page = ParentalKey("home.HomePage", related_name="social_images")
    social_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    link = models.URLField(blank=True, default='')
    name = models.CharField(max_length=255, help_text='Social platform')

    panels = [FieldPanel("name"), FieldPanel("social_image"), FieldPanel("link")]

# header links

# class HeaderLinks(Orderable):
#     page = ParentalKey("home.HomePage", related_name="header_links")
#     name = models.CharField(max_length=255)
#     link = models.URLField(blank=True, default='')

#     panels = [FieldPanel("name"), FieldPanel("link")]


# images for carousel banner

class HomePageCarouselImages(Orderable):
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    link = models.URLField(blank=True, default='')

    panels = [FieldPanel("carousel_image"), FieldPanel("link")]


# home page, including block containing artist roster

class HomePage(AbstractEmailForm):
    template = "home/home_page.html"

    intro = RichTextField(null=True, blank=True)
    thank_you_text = RichTextField(null=True, blank=True)

    # def get_context(self, request):
    #     context = super().get_context(request)
    #     length = len(HeaderLinks.objects.all())
    #     headers = HeaderLinks.objects.all()
    #     print(headers)

    roster = StreamField(
        [
            ('roster', RosterBlock())
        ],
        null=True,
        blank=False
    )
    
    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=3, min_num=3, label="Image")],
            heading="Carousel Images"), 
        MultiFieldPanel(
            [InlinePanel("social_images", max_num=8, min_num=3, label="Image")],
            heading="Social Links"),
        # MultiFieldPanel(
        #     [InlinePanel("header_links", max_num=8, min_num=4, label="Link")],
        #     heading="Header Links"),
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form Fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),  
        FieldPanel('roster')
    ]
