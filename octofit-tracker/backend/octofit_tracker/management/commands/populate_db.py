from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email
        db.users.create_index([('email', 1)], unique=True)

        # Teams
        teams = [
            {'name': 'Marvel', 'description': 'Team Marvel Superheroes'},
            {'name': 'DC', 'description': 'Team DC Superheroes'},
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {'user': 'spiderman@marvel.com', 'activity': 'Web Swinging', 'duration': 30},
            {'user': 'ironman@marvel.com', 'activity': 'Flight Training', 'duration': 45},
            {'user': 'batman@dc.com', 'activity': 'Martial Arts', 'duration': 60},
            {'user': 'wonderwoman@dc.com', 'activity': 'Lasso Practice', 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'user': 'spiderman@marvel.com', 'points': 100},
            {'user': 'ironman@marvel.com', 'points': 90},
            {'user': 'batman@dc.com', 'points': 95},
            {'user': 'wonderwoman@dc.com', 'points': 98},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user': 'spiderman@marvel.com', 'workout': 'Upper Body', 'reps': 50},
            {'user': 'ironman@marvel.com', 'workout': 'Cardio', 'reps': 40},
            {'user': 'batman@dc.com', 'workout': 'Strength', 'reps': 60},
            {'user': 'wonderwoman@dc.com', 'workout': 'Agility', 'reps': 55},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
