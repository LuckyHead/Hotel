from django.db.models import *

from apps.hotel.models import Hotel

class Room(Model):
    hotels=OneToOneField(
        Hotel,
        verbose_name='Hotel',
        on_delete=PROTECT
    )

    number=PositiveSmallIntegerField(
        'Number of the room'
    )

    capacity=PositiveSmallIntegerField(
        'Capacity of the room',
    )

    price_per_night=PositiveIntegerField(
        'Price'
    )

    is_used=BooleanField()

    descriprion=TextField(
        'About room'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Room'
        verbose_name_plural='Rooms'
