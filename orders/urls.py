from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'projects', views.ProjectsViewSet)
router.register(r'setups', views.SetupViewSet)
router.register(r'', views.OrderViewSet)

app_name = 'orders'
urlpatterns = [
    path('', include(router.urls)),
]
