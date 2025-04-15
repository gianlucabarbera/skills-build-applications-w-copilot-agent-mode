from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        self.assertEqual(user.username, "testuser")

# Aggiungi test simili per Team, Activity, Leaderboard e Workout
