from django.test import TestCase
from Posts.models import User,Comments,Likes,Posts
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def test_Posts_Likes_Comments(self):
        user1 = User.objects.create(username="django_test1", email="django_test1@abc.com", password="password12")
        posts = Posts.objects.create(
            Poster = user1,
            Content = "Sample Content",
            Caption = "Sample Caption",
            Event = "Sample Event",
            Time = '2020-10-25 14:30:59'
        )
        posts.save()
        self.assertEqual(str(Posts.objects.get(Poster=user1).Poster), "django_test1")
        self.assertEqual(str(Posts.objects.get(Poster=user1).Content), "Sample Content")

        likes = Likes.objects.create(
            LikedPostId = posts,
            LikerPid = user1,
        )
        likes.save()
        self.assertEqual(Likes.objects.get(LikedPostId=posts).LikedPostId, posts)
        self.assertEqual(str(Likes.objects.get(LikerPid=user1).LikerPid), "django_test1")

        comments = Comments.objects.create(
            LikedPostId = posts,
            LikerPid = user1,
            Comment = "Sample Comment",
            Time = '2020-10-25 14:30:59'
        )
        comments.save()
        self.assertEqual(Comments.objects.get(LikedPostId=posts).LikedPostId, posts)
        self.assertEqual(str(Comments.objects.get(LikerPid=user1).LikerPid), "django_test1")
        self.assertEqual(str(Comments.objects.get(LikerPid=user1).Comment), "Sample Comment")

        #   Update
        Posts.objects.filter(Poster=user1).update(Content = "New Sample Content")
        self.assertEqual(str(Posts.objects.get(Poster=user1).Content), "New Sample Content")

        Comments.objects.filter(LikerPid=user1).update(Comment = "New Sample Comment")
        self.assertEqual(str(Comments.objects.get(LikerPid=user1).Comment), "New Sample Comment")

        #   Delete
        Posts.objects.filter(Poster=user1).delete()
        self.assertEqual(Posts.objects.filter(Poster=user1).exists(), False)

        Likes.objects.filter(LikerPid=user1).delete()
        self.assertEqual(Likes.objects.filter(LikerPid=user1).exists(), False)