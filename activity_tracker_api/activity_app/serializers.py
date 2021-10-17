from django.db.models import Count
from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


class CommonActivitiesSerializer(serializers.ListSerializer):

    class Meta:
        model = Activity
        fields = ('common_items',)

    common_items = serializers.SerializerMethodField()

    def get_common_items(self, _):
        queryset = Activity.objects \
                    .values('type') \
                    .annotate(count=Count('type')) \
                    .order_by()
        return queryset
