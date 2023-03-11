import uuid
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class Order(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#uuidfield
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('orders:order-detail', kwargs={'pk': self.pk})


class Projects(models.Model):
    git = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "projects"

    def __str__(self):
        return f'Projects for {self.order}'

    def get_absolute_url(self):
        return reverse('orders:projects-detail', kwargs={'pk': self.pk})


class Setup(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'Setup for {self.order}'

    def get_absolute_url(self):
        return reverse('orders:setup-detail', kwargs={'pk': self.pk})
