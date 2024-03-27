from django.db.models import *
from apps.guest.models import Guest
from apps.room.models import Room

class Booking(Model):
    room=ManyToManyField(
        Room,
        verbose_name='Room',
    )

    guest=ManyToManyField(
        Guest,
        verbose_name='Guest',
    )

    check_in_date=DateTimeField(
        'Check in date',
        auto_now_add=True
    )

    check_out_date=DateTimeField(
        'Check out date',
        blank=True
    )

    is_paid=BooleanField(
        default=False
    )


    class Meta:
        verbose_name='booking'
        verbose_name_plural='bookings'