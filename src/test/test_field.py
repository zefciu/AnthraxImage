import os
import unittest

from anthrax.image.field import ImageField
from anthrax.container import Form

HERE = os.path.dirname(os.path.abspath(__file__))

class Test(unittest.TestCase):
    def setUp(self):
        class ImageForm(Form):
            image = ImageField(scale_down=(200, 200), directory=HERE)
        self.form = ImageForm()

    def test_scaled_down_entry(self):
        self.form.__raw__ = {'image': 'pythons.jpeg'}
        self.assertEqual(self.form['image'].width, 200)
        self.assertEqual(self.form['image'].height, 128)
        
        
