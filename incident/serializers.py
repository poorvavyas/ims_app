from rest_framework import serializers, status
from .models import Incident
from account.serializers import UserRetrieveSerializer
from django.utils import timezone
from rest_framework.response import Response


class IncidentRetrieveSerializer(serializers.ModelSerializer):
    reporter_name = UserRetrieveSerializer()

    class Meta:
        model = Incident
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = '__all__'

    def save(self, r, ins_obj):
        incident_id = Incident.objects.generate_incident_id()
        self.validated_data['incident_id'] = incident_id
        self.validated_data['reporter_name'] = r.user
        self.validated_data['report_date'] = timezone.now()
        return super().save()
