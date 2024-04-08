from rest_framework import viewsets, status
from rest_framework import permissions
from .models import Incident
from .serializers import IncidentSerializer, IncidentRetrieveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class IncidentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows incident to be viewed or edited.
    """
    queryset = Incident.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            serializer_class = IncidentSerializer
        else:
            serializer_class = IncidentRetrieveSerializer
        return serializer_class

    def get_queryset(self):
        queryset = Incident.objects.get_incident_by_user(self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(self.request, None)

    def update(self, request, pk):
        try:
            instance = self.get_object()
            if instance.incident_status != 'C':
                if request.data.get("incident_status") not in ['O', 'P', 'C']:
                    request.data['incident_status'] = 'O'
                instance.incident_status = request.data.get("incident_status")
                if request.data.get("priority") not in ['L', 'H', 'M']:
                    request.data['priority'] = 'L'
                instance.priority = request.data.get("priority")
                instance.incident_detail = request.data.get("incident_detail")
                instance.save()
                serializer = IncidentRetrieveSerializer(instance)
                message = "Updated Successfully"
            else:
                message = "Can't update closed incident"
                return Response(data={"message": message})
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": message, "incident": serializer.data})

    @action(detail=False, methods=['GET'], url_path='by_incident_id/(?P<id>[^/.]+)')
    def by_incident_id(self, request, id=None):
        try:
            queryset = Incident.objects.get_incident_by_id(id)
            serializer = IncidentRetrieveSerializer(queryset, many=True)
            if queryset:
                auth_user = Incident.objects.check_user_authorized(queryset[0].reporter_name, request.user)
                if auth_user:
                    return Response(serializer.data)
                else:
                    message = 'User not Authorized to access the incident.'
                    return Response({"message": message})
            else:
                message = 'No Such incident.'
                return Response({"message": message})
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
