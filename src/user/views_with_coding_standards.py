import json

from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.response import Response

from user.models import EmployeeDetails
from rest_framework import viewsets, status, exceptions
from user.serializers import EmployeeSerializer


class GetRequest(viewsets.ViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
    lookup_url_kwarg = None

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: kwargs[lookup_url_kwarg]}
        try:
            obj = self.queryset.get(**filter_kwargs)
        except self.queryset.model.DoesNotExist:
            raise exceptions.NotFound
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """For Posting Record"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """For Completely Updating Record"""
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: kwargs[lookup_url_kwarg]}

        try:
            obj = self.queryset.get(**filter_kwargs)
        except self.queryset.model.DoesNotExist:
            raise exceptions.NotFound
        serializer = self.serializer_class(obj, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """For Completely Updating Record"""
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: kwargs[lookup_url_kwarg]}
        try:
            obj = self.queryset.get(**filter_kwargs)
        except self.queryset.model.DoesNotExist:
            raise exceptions.NotFound
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """For Deleting the record"""
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: kwargs[lookup_url_kwarg]}
        try:
            obj = self.queryset.get(**filter_kwargs)
        except self.queryset.model.DoesNotExist:
            raise exceptions.NotFound
        obj.delete()
        return Response(status.HTTP_204_NO_CONTENT)
