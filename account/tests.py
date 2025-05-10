from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model
from messaging.models import Message

User = get_user_model()

class MessageModelTest(TestCase):

    def setUp(self):
        self.sender = User.objects.create_user(
            username='sender',
            password='password123',
            email='sender@example.com'
        )
        self.receiver = User.objects.create_user(
            username='receiver',
            password='password123',
            email='receiver@example.com'
        )

    def test_message_creation(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Hello, this is a test message.'
        )
        self.assertEqual(message.sender, self.sender)
        self.assertEqual(message.receiver, self.receiver)
        self.assertEqual(message.content, 'Hello, this is a test message.')
        self.assertTrue(message.timestamp)

    def test_reverse_relationships(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Another test message.'
        )
        self.assertIn(message, self.sender.sent_messages.all())
        self.assertIn(message, self.receiver.received_messages.all())
