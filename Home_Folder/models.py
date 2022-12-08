from django.db import models
import uuid
# Create your models here.
class QrUrl(models.Model):
    tableNumber = models.PositiveSmallIntegerField(primary_key=True, unique=True,)
    id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
    	return str(self.id)