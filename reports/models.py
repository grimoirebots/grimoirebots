import uuid
from django.db import models
from django.urls import reverse

from orders.models import Order


class Report(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#uuidfield
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    report = models.TextField(max_length=500, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.id.__str__()

    def get_absolute_url(self):
        return reverse('reports:report-detail', kwargs={'pk': self.pk})
