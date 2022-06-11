from django.test import TestCase
from Friends.models import FriendRequests,Friendship,User
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def test_Friendship(self):
        user1 = User.objects.create(username="django_test1", email="django_test1@abc.com", password="password12")
        user2 = User.objects.create(username="django_test2", email="django_test2@abc.com", password="password12")
        user1.save()
        user2.save()
        friendship = Friendship.objects.create(
            Friend_1 = user1,
            Friend_2 = user2,
        )
        friendship.save()
        self.assertEqual(str(Friendship.objects.get(Friend_1=user1).Friend_1), "django_test1")
        self.assertEqual(str(Friendship.objects.get(Friend_2=user2).Friend_2), "django_test2")

        #   Update
        Friendship.objects.filter(Friend_1=user1).update(Friend_1 = user2)  # swap friends
        Friendship.objects.filter(Friend_2=user2).update(Friend_2 = user1)
        self.assertEqual(str(Friendship.objects.get(Friend_2=user1).Friend_2), "django_test1")
        self.assertEqual(str(Friendship.objects.get(Friend_1=user2).Friend_1), "django_test2")

        #   Delete
        Friendship.objects.filter(Friend_1=user2).delete()
        Friendship.objects.filter(Friend_2=user1).delete()
        self.assertEqual(Friendship.objects.filter(Friend_1=user2).exists(), False)
        self.assertEqual(Friendship.objects.filter(Friend_2=user1).exists(), False)

