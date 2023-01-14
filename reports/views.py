from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    # https://www.django-rest-framework.org/api-guide/renderers/#varying-behaviour-by-media-type
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         if request.accepted_renderer.format == 'html':
    #             data = {'results': page}
    #             return Response(data, template_name='reports/report_list.html')
    #
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     if request.accepted_renderer.format == 'html':
    #         data = {'results': queryset}
    #         return Response(data, template_name='reports/report_list.html')
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #
    #     if request.accepted_renderer.format == 'html':
    #         data = {'report': instance}
    #         return Response(data, template_name='reports/report_detail.html')
    #
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
