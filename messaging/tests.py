from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model
from messaging.models import Message

User = get_user_model()

class MessageModelTest(TestCase):

    def setUp(self):
        # Create users for testing
        self.sender = User.objects.create_user(username='sender', password='password123')
        self.receiver = User.objects.create_user(username='receiver', password='password123')

    def test_message_creation(self):
        # Create a message instance
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Hello, this is a test message.'
        )

        # Retrieve the message from the database
        retrieved_message = Message.objects.get(id=message.id)

        # Assert the message content is correct
        self.assertEqual(retrieved_message.content, 'Hello, this is a test message.')

    def test_related_name_reverse_relation(self):
        # Create a message instance
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Another test message.'
        )

        # Access the related messages from the receiver's perspective
        received_messages = self.receiver.received_messages.all()

        # Assert the receiver has the correct number of messages
        self.assertEqual(received_messages.count(), 1)

        # Assert the content of the received message
        self.assertEqual(received_messages.first().content, 'Another test message.')
