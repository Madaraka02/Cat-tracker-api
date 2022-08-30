from django.db import models
import uuid
from timezone_field import TimeZoneField
import pytz



# Create your models here.
class Cat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500, null=True)
    color = models.CharField(max_length=500, null=True)
    zone = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name