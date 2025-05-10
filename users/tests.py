from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.exceptions import ValidationError

User = get_user_model()

class CustomUserModelTest(TestCase):
    
    def test_create_user_with_required_fields(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            bio="Just a test user."
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpass123"))
        self.assertEqual(user.bio, "Just a test user.")

    def test_handle_must_be_unique(self):
        User.objects.create_user(
            username="user1",
            password="pass1",
            handle="uniquehandle",
            bio="User 1"
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username="user2",
                password="pass2",
                handle="uniquehandle",  # same handle, should fail
                bio="User 2"
            )

    def test_display_name_optional(self):
        user = User.objects.create_user(
            username="nodefname",
            password="pass123",
            bio="Bio here."
        )
        self.assertEqual(user.display_name, "")  # default is blank
