from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Order, Projects, Setup
from .serializers import OrderSerializer, ProjectsSerializer, SetupSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False)
    def pending(self, request):
        queryset = Order.objects.filter(report=None)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, url_path='projects.json')
    def projects(self, request, pk=None):
        order = self.get_object()
        projects = order.projects

        serializer = ProjectsSerializer(projects)
        return Response(serializer.data)

    @action(detail=True, url_path='setup.cfg')
    def setup(self, request, pk=None):
        order = self.get_object()
        setup = order.setup

        serializer = SetupSerializer(setup)
        return Response(serializer.data)


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class SetupViewSet(ModelViewSet):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer
