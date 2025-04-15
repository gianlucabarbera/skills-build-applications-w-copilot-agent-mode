from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_data

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_data['users']:
            User.objects.get_or_create(**user_data)

        # Populate teams
        for team_data in test_data['teams']:
            members = team_data.pop('members', [])
            team, created = Team.objects.get_or_create(**team_data)
            for member_username in members:
                member = User.objects.get(username=member_username)
                team.members.add(member)

        # Populate activities
        for activity_data in test_data['activities']:
            user = User.objects.get(username=activity_data.pop('user'))
            Activity.objects.get_or_create(user=user, **activity_data)

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            user = User.objects.get(username=leaderboard_data.pop('user'))
            Leaderboard.objects.get_or_create(user=user, **leaderboard_data)

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout.objects.get_or_create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
