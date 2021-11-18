from rest_framework import serializers
from .models import Profile

# class UserGroup(serializers.ModelSerializer):
#     class Meta:
#         model = UserGroup
#         fields = '__all__'

class Profile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'