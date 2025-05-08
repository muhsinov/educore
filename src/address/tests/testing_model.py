import unittest
from address.models import Address

class TestAddress(unittest.TestCase):
    def test_address(self):
        address = Address.objects.create(
            street="test street",
            destrict="test district",
            region="test region"
        )

        self.assertEqual(address.street, "test street")
        self.assertEqual(address.destrict, "test district")
        self.assertEqual(address.region, "test region")