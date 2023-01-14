from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'', views.OrderViewSet)

app_name = 'orders'
urlpatterns = [
    path('', include(router.urls)),
]
