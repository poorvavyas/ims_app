from rest_framework import serializers
from django.contrib.auth.models import User as userModel


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    def save(self):
        """ Saving user Once data is validated. """
        user = userModel.objects.create_user(first_name=self.validated_data['first_name'],
                                             last_name=self.validated_data['last_name'],
                                             password=self.validated_data['password'],
                                             username=self.validated_data['username'],
                                             email=self.validated_data['email'])
        return user

