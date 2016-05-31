from django.db import models
from django.utils import timezone

class Item(models.Model):
    item_id = models.CharField(max_length=8, primary_key=True)
    description = models.CharField(max_length=128)
    group = models.CharField(max_length=32)
    status = models.CharField(max_length=16)
    location = models.CharField(max_length=16)
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(blank=True, null=True)
    last_mod_by = models.CharField(max_length=16)

    def modified(self):
        self.last_modified = timezone.now()
        self.save()

    def __str__(self):
        return self.description

    #user = models.ForeignKey('auth.User')
