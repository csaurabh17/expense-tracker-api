from django.urls import path
from restapi import views

urlpatterns = [path("expenses/", views.CreateExpense.as_view(), name="create-expenses")]
