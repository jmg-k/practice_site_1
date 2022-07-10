from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ArtistBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    link = blocks.URLBlock(required=True)

class RosterBlock(blocks.StructBlock):

    class Meta:
        template = 'blocks/roster.html'

    artists = blocks.ListBlock(
        ArtistBlock()
    )
