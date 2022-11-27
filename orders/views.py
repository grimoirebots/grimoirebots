from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import Order
from .serializers import OrderSerializer


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


class OrderJSON(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class EarliestOrderJSON(ListAPIView):
    queryset = Order.objects.all().order_by('pub_date')
    serializer_class = OrderSerializer
