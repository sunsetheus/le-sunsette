from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_assign_item(self):
        Item.objects.create(
            name = 'Plain croissant',
            amount = 6,
            description = 'Classic type croissant with layers of buttery dough, each bite reveals a harmony of flaky and melted buttery. Savor the simplicity of pure delight – the perfect companion to your morning coffee or a snack',
            price = 2.2
        )
        plain_croissant = Item.objects.get(name = 'Plain croissant')
        self.assertEqual(plain_croissant.amount, 6)
        self.assertEqual(plain_croissant.description, 'Classic type croissant with layers of buttery dough, each bite reveals a harmony of flaky and melted buttery. Savor the simplicity of pure delight – the perfect companion to your morning coffee or a snack')
        self.assertEqual(plain_croissant.price, 2.2)