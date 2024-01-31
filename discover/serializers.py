from django.contrib.auth.models import Group, User
from rest_framework import serializers
from discover.models import DiscoverThread, Source
from django.utils import timezone
from django.template.defaultfilters import timesince

class DiscoverThreadSerializer(serializers.HyperlinkedModelSerializer):
    time_since_posted = serializers.SerializerMethodField()

    class Meta:
        model = DiscoverThread
        fields = ['id', 'title', 'description', 'views', 'branches', 'image_url', 'time_since_posted']

    def get_time_since_posted(self, obj):
        return timesince(obj.datetime, timezone.now())

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['url']

class ThreadDetailSerializer(serializers.HyperlinkedModelSerializer):
    time_since_posted = serializers.SerializerMethodField()
    sources = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = DiscoverThread
        fields = ['id', 'title', 'description', 'views', 'branches', 'image_url', 'time_since_posted', 'sources']

    def get_time_since_posted(self, obj):
        return timesince(obj.datetime, timezone.now())