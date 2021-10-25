from django.db.models import Count
from django.http import JsonResponse
from rest_framework import generics, views
from .serializers import ActivitySerializer, CommonActivitiesSerializer
from .models import Activity
from .authentication import BearerTokenAuthentication


class ActivityListView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


activity_list_view = ActivityListView.as_view()


class CommonActivitiesView(views.APIView):

    @staticmethod
    def get(request):
        queryset = Activity.objects \
                    .values('type') \
                    .annotate(count=Count('type')) \
                    .order_by('count').reverse()

        qs_list = list(queryset)
        return JsonResponse(qs_list, safe=False)


common_activities_view = CommonActivitiesView.as_view()
