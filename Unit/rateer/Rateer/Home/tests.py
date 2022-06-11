from django.test import TestCase
from Home.models import Feedback, Person, Privacy
from django.contrib.auth.models import User


# Unit Views Testing done by Abubakar Siddique
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_HomeView(self):
        response = self.client.get(reverse('Home:HomeView'))
        self.assertTemplateUsed(response, 'HomeTemplate.html')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_ContactView_GET(self):
        response = self.client.get(reverse('Home:ContactView'))
        self.assertTemplateUsed(response, 'ContactUs.html')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_AboutView(self):
        response = self.client.get(reverse('Home:AboutView'))
        self.assertTemplateUsed(response, 'AboutUs.html')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_SignInView(self):
        response = self.client.get(reverse('Home:SignInView'))
        self.assertTemplateUsed(response, 'SignIn.html')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_SignUpView(self):
        response = self.client.get(reverse('Home:SignUpView'))
        self.assertTemplateUsed(response, 'SignUp.html')
        self.assertEquals(response.status_code, HTTPStatus.OK)



class TestModels(TestCase):
    def test_Person(self):
        user = User.objects.create(username="django_test", email="django_test@abc.com", password="password12")
        user.save()
        person = Person.objects.create(
            ThisUser = user,
            Age = 12,
            Status = "Alive",
            Address = "221 Street london",
            Phone = "+1-777-777",
            Profession = "Software Tester"
        )
        person.save()
        self.assertEqual(str(Person.objects.get(ThisUser=user)), "django_test")
        self.assertEqual(Person.objects.get(ThisUser=user).Status, "Alive")
        #   Update
        Person.objects.filter(ThisUser=user).update(Status = "Deceased")
        self.assertEqual(Person.objects.get(ThisUser=user).Status, "Deceased")
        #   Delete
        Person.objects.filter(ThisUser=user).delete()
        self.assertEqual(Person.objects.filter(ThisUser=user).exists(), False)

    def test_Feedback(self):
        feedback = Feedback.objects.create(
            UserName = "django_test",
            Subject = "django_Subject",
            Message = "django_Message",
        )
        feedback.save()
        self.assertEqual(str(Feedback.objects.get(UserName="django_test").UserName), "django_test")
        #   Update
        Feedback.objects.filter(UserName="django_test").update(UserName = "new_django_test")
        self.assertEqual(Feedback.objects.get(UserName="new_django_test").UserName, "new_django_test")
        #   Delete
        Feedback.objects.filter(UserName="django_test").delete()
        self.assertEqual(Feedback.objects.filter(UserName="django_test").exists(), False)


    def test_Privacy(self):
        user = User.objects.create(username="django_test", email="django_test@abc.com", password="password12")
        user.save()
        privacy = Privacy.objects.create(
            ThisUser = user,
            Email = True,
            Age = True,
            Address = True,
            Phone = True,
            Profession = True,
            Educations = True,
            Hobbies = True,
        )
        privacy.save()
        self.assertEqual(str(Privacy.objects.get(ThisUser=user).ThisUser), "django_test")
        #   Update
        Privacy.objects.filter(ThisUser=user).update(Age = False)
        self.assertEqual(Privacy.objects.get(ThisUser=user).Age, False)
        #   Delete
        Privacy.objects.filter(ThisUser=user).delete()
        self.assertEqual(Privacy.objects.filter(ThisUser=user).exists(), False)
