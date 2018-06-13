from django.db import models
import uuid

class Shortly(models.Model):
    url_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    url = models.CharField(max_length=250, unique=True)
    visited = models.IntegerField(default=0)