import json

from django.core.serializers import serialize
from django.http import JsonResponse

from user.models import EmployeeDetails
from rest_framework import viewsets

class GetRequest(viewsets.ViewSet):

    def listk(self, request):

        det = EmployeeDetails.objects.all()  # det will be of type queryset
        serialize_data = serialize("json", det)  # serialize function will convert querset to str
        serialized_data = json.loads(serialize_data)  # json.loads will convert to str to list
        return JsonResponse(serialized_data, safe=False)  # JSONResponse will convert list to JSON object

    def retrieve(self,request,pk=None):
        det = EmployeeDetails.objects.filter(id=pk)
        serialize_data = serialize("json", det)
        serialize_data = json.loads(serialize_data)
        return JsonResponse(serialize_data, safe=False)

    def create(self, request):
        """For Posting Record"""

        data = json.loads(request.body)
        EmployeeDetails.objects.create(**data)
        return JsonResponse({"Employee": "added"})

    def update(self, request, pk=None):

        """For Completely Updating Record"""
        det = EmployeeDetails.objects.get(id=pk)
        data = json.loads(request.body)
        det.name = data["name"]
        det.department = data["department"]
        det.save()
        return JsonResponse({"employee": "updated"})


    def destroy(self,request,pk=None):
        """For Deleting the record"""

        emp = EmployeeDetails.objects.get(id=pk)
        emp.delete()
        return JsonResponse({"Employee": "removed"})

