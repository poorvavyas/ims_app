from django.db.models import Q
from django.db import models
from datetime import date
from django.core.exceptions import ObjectDoesNotExist


class IncidentQuerySet(models.QuerySet):
    def get_incident_by_user(self, user_id):
        """
        Queryset to get incident by user
        :param user_id: int
        :return: List of incident Objects
        """

        return self.filter(reporter_name=user_id)

    def get_incident_by_id(self, id):
        """
        Queryset to get incident by id
        :param incident_id: int
        :return: List of incident Objects
        """

        return self.filter(incident_id=id)

    def check_user_authorized(self, incident_user, req_user):
        return incident_user == req_user
        # pass

    def generate_incident_id(self):
        """
        Queryset to generate incident id
        :return: Custom incident id
        """
        current_year = date.today().year
        try:
            id = self.latest('pk').pk + 1
        except ObjectDoesNotExist:
            id = 1
        id = "RMG%05d" % id + str(current_year)
        return id
