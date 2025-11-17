from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.filter(pk__isnull=False).delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = []
        users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team_name='Marvel'))
        users.append(User.objects.create(name='Captain America', email='cap@marvel.com', team_name='Marvel'))
        users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team_name='Marvel'))
        users.append(User.objects.create(name='Batman', email='batman@dc.com', team_name='DC'))
        users.append(User.objects.create(name='Superman', email='superman@dc.com', team_name='DC'))
        users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team_name='DC'))

        # Activities
        Activity.objects.create(user_email='ironman@marvel.com', type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user_email='batman@dc.com', type='Cycling', duration=45, date=timezone.now().date())

        # Workouts
        Workout.objects.create(name='Push Ups', description='Upper body exercise', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Lower body exercise', difficulty='Easy')

        # Leaderboard
        Leaderboard.objects.create(team_name='Marvel', points=150)
        Leaderboard.objects.create(team_name='DC', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
