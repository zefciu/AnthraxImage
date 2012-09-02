from gettext import gettext as _

import pystacia
from pystacia.util import TinyException

from anthrax.field.file import FileField
from anthrax.exc import ValidationError

class ImageField(FileField):
    """File subclass handling images. Uses pystacia to parse and resize images.
"""

    accept_mime = {'image/*'}
    scale_down = None

    def to_python(self, value):
        value = super(ImageField, self).to_python(value)
        try:
            img = pystacia.read_blob(value.file.read())
        except TinyException:
            raise ValidationError(_('Cannot read the image'))
        if self.scale_down is not None:
            to_width, to_height = self.scale_down
            factor = min(to_width/img.width, to_height/img.height)
            if factor < 1:
                img.rescale(factor=factor)
        return img

    def validate_python(self, value):
        """We suppress the baseclass validation, cause we no longer deal with
        file object."""
