from django.test import TestCase
from restapi import models
from django.urls import reverse

# Create your tests here.


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=200, vendor="dmart", description="grocery", category="household"
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(200, inserted_expense.amount)
        self.assertEqual("dmart", inserted_expense.vendor)


class TestViews(TestCase):
    def test_create_expense(self):
        payload = {
            "amount": 100,
            "vendor": "Samsung",
            "description": "Mobile phone accessory",
            "category": "Accessories",
        }

        res = self.client.post(
            reverse("restapi:create-expenses"), payload, format="json"
        )

        self.assertEqual(201, res.status_code)

        resp = res.json()
        self.assertEqual(payload["vendor"], resp["vendor"])
        self.assertIsInstance(resp["id"], int)
