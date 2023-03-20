from rest_framework import serializers
from user.models import EmployeeDetails


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = "__all__"
