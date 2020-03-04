import io
from typing import Type

from PIL import Image
from django.core.files import File
from mixer.backend.django import mixer

from photosets.models import Photoset, Photo


class CycleFactory:
    def __init__(self, factory: 'Type[Factory]', count: int):
        self.factory = factory
        self.count = count

    def __getattr__(self, name):
        if hasattr(self.factory, name):
            return lambda *args, **kwargs: [
                getattr(self.factory, name)(*args, **kwargs) for _ in range(0, self.count)
            ]


class Factory:
    @classmethod
    def cycle(cls, count):
        """
        Run given method X times:
            Factory.cycle(5).orderItem()  # gives 5 orders
        """
        return CycleFactory(cls, count)

    @classmethod
    def image(cls, size=(60, 30), color='purple', format='JPEG'):
        out = io.BytesIO()
        img = Image.new('RGB', size, color=color)
        img.save(out, format)
        return out

    @classmethod
    def photoset(cls, create_photos=0, create_preview=False, preview=None, **kwargs) -> Photoset:
        if preview is None:
            preview = cls.image()

        photoset = mixer.blend('photosets.Photoset', **kwargs)
        if create_preview:
            preview = File(preview)
            photoset.preview.save('image.jpg', preview, save=True)

        cls.cycle(create_photos).photo(photoset=photoset)
        photoset.refresh_from_db()
        return photoset

    @classmethod
    def photo(cls, image=None, crop='', **kwargs) -> Photo:
        if image is None:
            image = cls.image()
        image = File(image)
        photo = mixer.blend('photosets.Photo', image=None, crop=crop, **kwargs)
        photo.image.save('image.jpg', image, save=True)
        return photo
