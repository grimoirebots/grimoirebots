import uuid
from django.db import models
from django.urls import reverse


class Order(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#uuidfield
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_source_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.id.__str__()

    def get_absolute_url(self):
        return reverse('orders:order-detail', kwargs={'pk': self.pk})
