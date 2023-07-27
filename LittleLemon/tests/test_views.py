from django.test import TestCase
from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItem.objects.create(title="AAA", price=11.1, inventory=1)
        self.item2 = MenuItem.objects.create(title="BBB", price=22.2, inventory=2)
        self.item3 = MenuItem.objects.create(title="CCC", price=33.3, inventory=3)

    def test_getall(self):
        aaa = MenuItem.objects.get(title="AAA")
        bbb = MenuItem.objects.get(title="BBB")
        ccc = MenuItem.objects.get(title="CCC")

        self.assertEqual(str(aaa), "AAA : 11.10")
        self.assertEqual(str(bbb), "BBB : 22.20")
        self.assertEqual(str(ccc), "CCC : 33.30")
