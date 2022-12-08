from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),
    path('new', views.OrderCreateView.as_view(), name='order-create'),
    path('<uuid:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('<uuid:pk>/update', views.OrderUpdateView.as_view(), name='order-update'),
    path('<uuid:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'),
    path('<uuid:pk>/projects.json', views.OrderJSON.as_view(), name='order-json'),
    path('earliest', views.EarliestOrderJSON.as_view(), name='earliest-order-json'),
]
