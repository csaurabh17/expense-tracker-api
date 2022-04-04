from django.test import TestCase
from restapi import models

# Create your tests here.


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=200, vendor="dmart", description="grocery", category="household"
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(200, inserted_expense.amount)
        self.assertEqual("dmart", inserted_expense.vendor)
