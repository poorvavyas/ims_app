from django import forms
from ..models import Incident
from django.contrib.auth.models import User as user_model


class IncidentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Initializing Form with values. """
        action = kwargs.pop('action')
        user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
        if action == 'add':
            id = Incident.objects.generate_incident_id()
            self.fields['incident_id'].initial = id
        self.fields['reporter_name'].queryset = user_model.objects.filter(pk=user.id)
        self.fields['reporter_name'].initial = user
        self.fields['incident_status'].readonly = True

    class Meta:
        model = Incident
        fields = '__all__'

        widgets = {
            'incident_id': forms.TextInput(attrs= {'class': 'form-control', 'readonly': True}),
            'reporter_name': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'incident_detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 5, 'required': True}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'incident_status': forms.Select(attrs={'class': 'form-control'}),
            'report_date': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': True}),
        }
