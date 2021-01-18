from django.db import models
from django.utils import timezone

from utils import TimeStampModel

class Reservation(models.Model):
    status = models.CharField(max_length = 20, default = "pending")
    people = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete = models.CASCADE)
    reservation_type = models.CharField(max_length = 20)
    package = models.ForeignKey("spaces.Package", on_delete = models.CASCADE)
    time = models.ForeignKey("Time", on_delete = models.CASCADE)

    class Meta:
        db_table = "reservations"

class Time(TimeStampModel):
    day = models.DateField(default = timezone.now)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    detail_space = models.ForeignKey("spaces.DetailSpace", on_delete = models.CASCADE)

    class Meta:
        db_table = "times"

class TimeType(models.Model):
    type_price = models.CharField(max_length = 45)
    