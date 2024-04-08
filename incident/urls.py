from django.urls import path
from incident.api import AddIncident, UpdateIncident, IncidentList


urlpatterns = [

    path('incident_list/', IncidentList.as_view(), name='incident_list'),
    path('add_incident/', AddIncident.as_view(), name='add_incident'),
    path('update_incident/<pk>/', UpdateIncident.as_view(), name='update_incident'),
]
