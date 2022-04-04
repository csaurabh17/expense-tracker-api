from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models
from django.forms.models import model_to_dict

# Create your views here.


class CreateExpense(APIView):
    def get(self, request):
        return Response(model_to_dict(models.Expense.object.all()), 200)

    def post(self, request):

        expense_obj = models.Expense.objects.create(
            amount=request.data["amount"],
            vendor=request.data["vendor"],
            description=request.data["description"],
            category=request.data["category"],
        )
        return Response(model_to_dict(expense_obj), 201)
