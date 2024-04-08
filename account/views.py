from django.contrib.auth.models import User as userModel
from rest_framework import viewsets
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = userModel.objects.all()
    serializer_class = UserSerializer
