from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'', views.ReportViewSet)

app_name = 'reports'
urlpatterns = [
    path('', include(router.urls)),
]
