from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Listing

class ListingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.listing = Listing.objects.create(
            user=self.user,
            title='Test Listing',
            description='This is a test listing.',
            category='Test Category',
            condition='new'
        )

    def test_listing_creation(self):
        self.assertEqual(self.listing.title, 'Test Listing')
        self.assertEqual(self.listing.description, 'This is a test listing.')
        self.assertEqual(self.listing.category, 'Test Category')
        self.assertEqual(self.listing.condition, 'new')
        self.assertEqual(self.listing.user.username, 'testuser')

class ListingCreateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_listing(self):
        response = self.client.post(reverse('create_listing'), {
            'title': 'New Listing',
            'description': 'Description of new listing',
            'category': 'New Category',
            'condition': 'new'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Listing.objects.count(), 1)  
        self.assertEqual(Listing.objects.get().title, 'New Listing')
        
class ListingEditTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.listing = Listing.objects.create(
            user=self.user,
            title='Old Title',
            description='Old description',
            category='Old Category',
            condition='used'
        )

    def test_edit_listing(self):
        response = self.client.post(reverse('edit_listing', args=[self.listing.id]), {
            'title': 'Updated Title',
            'description': 'Updated description',
            'category': 'Updated Category',
            'condition': 'new'
        })
        self.assertEqual(response.status_code, 302)  
        self.listing.refresh_from_db()  
        self.assertEqual(self.listing.title, 'Updated Title')  

class ListingDetailTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.listing = Listing.objects.create(
            user=self.user,
            title='Detail Title',
            description='Detail description',
            category='Detail Category',
            condition='new'
        )

    def test_listing_detail_view(self):
        response = self.client.get(reverse('listing_detail', args=[self.listing.id]))
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Detail Title')  
        self.assertContains(response, 'Detail description')  
