from django.test import TestCase
from Messenger.models import Messages,User
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def test_Friendship(self):
        user1 = User.objects.create(username="django_test1", email="django_test1@abc.com", password="password12")
        user2 = User.objects.create(username="django_test2", email="django_test2@abc.com", password="password12")
        user1.save()
        user2.save()
        messages = Messages.objects.create(
            Sender = user1,
            Receiver = user2,
            Message = "Sample message",
            Time = '2020-10-25 14:30:59'
        )
        messages.save()
        self.assertEqual(str(Messages.objects.get(Sender=user1).Sender), "django_test1")
        self.assertEqual(str(Messages.objects.get(Receiver=user2).Receiver), "django_test2")

        #   Update
        Messages.objects.filter(Sender=user1).update(Message = "New Sample Message")
        self.assertEqual(str(Messages.objects.get(Sender=user1).Message), "New Sample Message")

        #   Delete
        Messages.objects.filter(Sender=user1).delete()
        self.assertEqual(Messages.objects.filter(Sender=user1).exists(), False)