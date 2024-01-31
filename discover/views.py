from django.contrib.auth.models import Group, User
from django.template.defaultfilters import timesince
from rest_framework import permissions, viewsets
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from discover.serializers import DiscoverThreadSerializer, ThreadDetailSerializer
from discover.models import DiscoverThread

class DiscoverThreadViewSet(viewsets.ModelViewSet):
    queryset = DiscoverThread.objects.all()
    serializer_class = DiscoverThreadSerializer

class ThreadDetailViewSet(viewsets.ModelViewSet):
    queryset = DiscoverThread.objects.all()
    serializer_class = ThreadDetailSerializer

    def list(self, request, *args, **kwargs):
        param_id = request.GET.get('id')

        if param_id:
            instance = get_object_or_404(self.queryset, id=param_id)
            serializer = self.serializer_class(instance)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)