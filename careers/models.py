from datetime import datetime
from django.db import models


class Careers(models.Model):
    username = models.CharField(max_length=100, unique=True)
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=150)

    def __repr__(self) -> str:
        return f"Career - id: {self.id}"
