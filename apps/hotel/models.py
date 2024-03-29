from django.db.models import *
from apps.guest.models import Guest
class Hotel(Model):

    name = CharField(max_length=128)
    address = CharField(max_length=256)
    city = CharField(max_length=64)
    rating = DecimalField(max_digits=2, decimal_places=1)
    image = ImageField(upload_to="hotel_images")
    about = TextField()

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
    

class Room(Model):
    hotel = ForeignKey(Hotel, on_delete=CASCADE)
    number = PositiveSmallIntegerField()
    capacity = PositiveSmallIntegerField()
    price_per_night = PositiveIntegerField()
    is_used = BooleanField(default=False)
    description = TextField()

    def __str__(self):
        return f"Room - {self.number}"
    class Meta:
        verbose_name = "Room",
        verbose_name_plural = "Rooms"

class Booking(Model):
    room = ForeignKey(Room, on_delete=CASCADE)
    guest = ForeignKey(Guest, on_delete=CASCADE)
    check_in_date = DateField(auto_now=True)
    check_out_date = DateField(auto_now_add=True, blank=True, null=True)
    is_paid = BooleanField(default=False)