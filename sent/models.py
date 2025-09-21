# models.py

from django.db import models

class SentModel(models.Model):
    sent_address = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sent_address} sent ✅'"






