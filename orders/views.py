from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Order


class OrderListView(ListView):
    model = Order
    paginate_by = 5
    ordering = ["-pub_date"]


class OrderDetailView(DetailView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = ["data_source_url"]


class OrderUpdateView(UpdateView):
    model = Order
    fields = ["data_source_url"]


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("orders:order-list")
