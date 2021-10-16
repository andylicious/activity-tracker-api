from rest_framework import generics
from .serializers import ActivitySerializer
from .models import Activity


class ActivityListView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


activity_list_view = ActivityListView.as_view()
