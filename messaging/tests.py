from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model
from messaging.models import Message

User = get_user_model()

class MessageModelTest(TestCase):

    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='password123')
        self.receiver = User.objects.create_user(username='receiver', password='password123')

    def test_message_creation(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Hello, this is a test message.'
        )

        retrieved_message = Message.objects.get(id=message.id)
        self.assertEqual(retrieved_message.content, 'Hello, this is a test message.')

    def test_related_name_reverse_relation(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Another test message.'
        )
        
        received_messages = self.receiver.received_messages.all()
        self.assertEqual(received_messages.count(), 1)
        self.assertEqual(received_messages.first().content, 'Another test message.')
