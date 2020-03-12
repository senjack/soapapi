from django.test import TestCase
from refactory.models import Administrator

class TestModels(TestCase):
    def setUp(self):
        self.new_admin = Administrator.objects.create(
            
        )

    def test_administrator_creation(self):
        self.assertEquals()

