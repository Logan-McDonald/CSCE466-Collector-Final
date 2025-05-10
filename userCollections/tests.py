from django.test import TestCase
from django.contrib.auth import get_user_model
from userCollections.models import Collection, Item

User = get_user_model()

class CollectionItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="pass123",
            bio="Test bio"
        )
        self.collection = Collection.objects.create(
            user=self.user,
            title="Test Collection"
        )

    def test_collection_creation(self):
        self.assertEqual(self.collection.title, "Test Collection")
        self.assertEqual(str(self.collection), "Test Collection")
        self.assertEqual(self.collection.user.username, "tester")

    def test_item_creation(self):
        item = Item.objects.create(
            collection=self.collection,
            name="Test Item",
            description="This is a test item."
        )
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(str(item), "Test Item")
        self.assertEqual(item.collection, self.collection)
        self.assertFalse(bool(item.image)) 

    def test_item_with_image_optional(self):
        item = Item.objects.create(
            collection=self.collection,
            name="Image Item",
            description="Has image",
            image=None
        )
        self.assertEqual(item.name, 'Image Item') 
        self.assertFalse(bool(item.image))
