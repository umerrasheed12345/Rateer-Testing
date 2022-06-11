from django.test import TestCase
from Dashboard.models import Education, Hobbies, NotificationStatus, Ratings, User
from django.contrib.auth.models import User


# Create your tests here.

class TestModels(TestCase):
    def test_Education(self):
        user = User.objects.create(username="django_test", email="django_test@abc.com", password="password12")
        user.save()
        education = Education.objects.create(
            ThisUser=user,
            Degree="BSCS",
            Institute="FAST Lahore",
            From="2020-05-05",
            Till="2022-05-05",
        )
        education.save()
        self.assertEqual(str(Education.objects.get(ThisUser=user).ThisUser), "django_test")
        self.assertEqual(str(Education.objects.get(ThisUser=user).Degree), "BSCS")
        self.assertEqual(str(Education.objects.get(ThisUser=user).Institute), "FAST Lahore")

        Education.objects.filter(ThisUser=user).update(Degree="MSCS")
        self.assertEqual(str(Education.objects.get(ThisUser=user).Degree), "MSCS")

        Education.objects.filter(ThisUser=user).delete()
        self.assertEqual(Education.objects.filter(ThisUser=user).exists(), False)

    def test_Hobbies(self):
        user = User.objects.create(username="django_test", email="django_test@abc.com", password="password12")
        user.save()
        hobbies = Hobbies.objects.create(
            ThisUser=user,
            Hobby="Tech Documentaries"
        )
        hobbies.save()
        self.assertEqual(str(Hobbies.objects.get(ThisUser=user).ThisUser), "django_test")
        self.assertEqual(str(Hobbies.objects.get(ThisUser=user).Hobby), "Tech Documentaries")

        Hobbies.objects.filter(ThisUser=user).update(Hobby="Literature Documentaries")
        self.assertEqual(str(Hobbies.objects.get(ThisUser=user).Hobby), "Literature Documentaries")

        Hobbies.objects.filter(ThisUser=user).delete()
        self.assertEqual(Hobbies.objects.filter(ThisUser=user).exists(), False)

    def test_Ratings(self):
        user1 = User.objects.create(username="django_test1", email="django_test1@abc.com", password="password12")
        user2 = User.objects.create(username="django_test2", email="django_test2@abc.com", password="password12")
        user1.save()
        user2.save()
        ratings = Ratings.objects.create(
            RatedPid=user1,
            RaterPid=user2,
            Rating=3,
        )
        ratings.save()
        self.assertEqual(str(Ratings.objects.get(RatedPid=user1).RatedPid), "django_test1")
        self.assertEqual(str(Ratings.objects.get(RaterPid=user2).RaterPid), "django_test2")
        self.assertEqual(Ratings.objects.get(RaterPid=user2).Rating, 3)

        Ratings.objects.filter(RatedPid=user1).update(Rating=1)
        self.assertEqual(Ratings.objects.get(RaterPid=user2).Rating, 1)

        Ratings.objects.filter(RatedPid=user1).delete()
        self.assertEqual(Ratings.objects.filter(RatedPid=user1).exists(), False)

    def test_NotificationStatus(self):
        user = User.objects.create(username="django_test", email="django_test@abc.com", password="password12")
        user.save()
        notificationStatus = NotificationStatus.objects.create(
            ThisUser=user,
            Messenger=True,
            Requests=True,
            Feed=False
        )
        notificationStatus.save()
        self.assertEqual(str(NotificationStatus.objects.get(ThisUser=user).ThisUser), "django_test")
        self.assertEqual(NotificationStatus.objects.get(ThisUser=user).Messenger, True)
        self.assertEqual(NotificationStatus.objects.get(ThisUser=user).Requests, True)
        self.assertEqual(NotificationStatus.objects.get(ThisUser=user).Feed, False)

        NotificationStatus.objects.filter(ThisUser=user).update(Messenger=False)
        self.assertEqual(NotificationStatus.objects.get(ThisUser=user).Messenger, False)
        NotificationStatus.objects.filter(ThisUser=user).update(Requests=False)
        self.assertEqual(NotificationStatus.objects.get(ThisUser=user).Requests, False)

        NotificationStatus.objects.filter(ThisUser=user).delete()
        self.assertEqual(NotificationStatus.objects.filter(ThisUser=user).exists(), False)
