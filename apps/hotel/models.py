from django.db.models import *


class Hotel(Model):
    name=CharField(
        'Hotel',
        max_length=256
    )

    address=CharField(
        'Address of the hotel',
        max_length=256
    )

    city=CharField(
        'City',
        max_length=256
    )

    country=CharField(
        'Country',
        max_length=256
    )

    rating=DecimalField(
        'Rating of the hotel',
        max_digits=2,
        decimal_places=1
    )

    image=ImageField(
        'View of the hotel',
        upload_to='hotel-images/'
    )

    description=TextField(
        'About hotel'
    )

    def __str__(self):
        return f'{self.name}'
    
    
    class Meta:
        verbose_name='hotel'
        verbose_name_plural='hotels'

