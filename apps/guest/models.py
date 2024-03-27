from django.db.models import *
from django.contrib.auth.models import AbstractUser


class Guest(AbstractUser):
    phone_number=CharField(
        'Phone number',
        max_length=13,
    )

    passport_serie=CharField(
        'Passport serie',
        max_length=9,
)

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name='guest'
        verbose_name_plural='guests'
