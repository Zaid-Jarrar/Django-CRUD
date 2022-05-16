from django.test import TestCase
from django.urls import reverse,reverse_lazy

# Create your tests here.

class SnackTest(TestCase):
    def test_snack_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')
        
    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_snack_create(self):
        url = reverse('create_snack')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_create.html')
        self.assertTemplateUsed(response, '_base.html')
    
    def test_snack_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')


