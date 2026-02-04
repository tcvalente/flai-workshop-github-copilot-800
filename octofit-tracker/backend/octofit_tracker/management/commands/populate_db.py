from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from users.models import User
from teams.models import Team
from activities.models import Activity
from leaderboard.models import Leaderboard
from workouts.models import Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League Champions'
        )
        
        # Create Users - Marvel Team
        self.stdout.write('Creating Marvel users...')
        iron_man = User.objects.create(
            email='tony.stark@marvel.com',
            name='Tony Stark',
            password='ironman123',
            team=team_marvel
        )
        captain_america = User.objects.create(
            email='steve.rogers@marvel.com',
            name='Steve Rogers',
            password='captainamerica123',
            team=team_marvel
        )
        black_widow = User.objects.create(
            email='natasha.romanoff@marvel.com',
            name='Natasha Romanoff',
            password='blackwidow123',
            team=team_marvel
        )
        hulk = User.objects.create(
            email='bruce.banner@marvel.com',
            name='Bruce Banner',
            password='hulk123',
            team=team_marvel
        )
        thor = User.objects.create(
            email='thor.odinson@marvel.com',
            name='Thor Odinson',
            password='thor123',
            team=team_marvel
        )
        
        # Create Users - DC Team
        self.stdout.write('Creating DC users...')
        superman = User.objects.create(
            email='clark.kent@dc.com',
            name='Clark Kent',
            password='superman123',
            team=team_dc
        )
        batman = User.objects.create(
            email='bruce.wayne@dc.com',
            name='Bruce Wayne',
            password='batman123',
            team=team_dc
        )
        wonder_woman = User.objects.create(
            email='diana.prince@dc.com',
            name='Diana Prince',
            password='wonderwoman123',
            team=team_dc
        )
        flash = User.objects.create(
            email='barry.allen@dc.com',
            name='Barry Allen',
            password='flash123',
            team=team_dc
        )
        aquaman = User.objects.create(
            email='arthur.curry@dc.com',
            name='Arthur Curry',
            password='aquaman123',
            team=team_dc
        )
        
        # Create Activities - Marvel Team
        self.stdout.write('Creating Marvel activities...')
        activities_data = [
            # Iron Man
            {'user': iron_man, 'type': 'running', 'duration': 45, 'calories': 500, 'distance': 8.0, 'days_ago': 1},
            {'user': iron_man, 'type': 'weightlifting', 'duration': 60, 'calories': 400, 'distance': None, 'days_ago': 2},
            {'user': iron_man, 'type': 'cycling', 'duration': 90, 'calories': 750, 'distance': 25.0, 'days_ago': 3},
            
            # Captain America
            {'user': captain_america, 'type': 'running', 'duration': 60, 'calories': 650, 'distance': 10.0, 'days_ago': 1},
            {'user': captain_america, 'type': 'weightlifting', 'duration': 75, 'calories': 500, 'distance': None, 'days_ago': 1},
            {'user': captain_america, 'type': 'running', 'duration': 55, 'calories': 600, 'distance': 9.5, 'days_ago': 2},
            
            # Black Widow
            {'user': black_widow, 'type': 'yoga', 'duration': 50, 'calories': 250, 'distance': None, 'days_ago': 1},
            {'user': black_widow, 'type': 'running', 'duration': 40, 'calories': 450, 'distance': 7.0, 'days_ago': 2},
            {'user': black_widow, 'type': 'weightlifting', 'duration': 45, 'calories': 350, 'distance': None, 'days_ago': 3},
            
            # Hulk
            {'user': hulk, 'type': 'weightlifting', 'duration': 90, 'calories': 700, 'distance': None, 'days_ago': 1},
            {'user': hulk, 'type': 'weightlifting', 'duration': 85, 'calories': 680, 'distance': None, 'days_ago': 2},
            {'user': hulk, 'type': 'running', 'duration': 30, 'calories': 400, 'distance': 5.0, 'days_ago': 3},
            
            # Thor
            {'user': thor, 'type': 'weightlifting', 'duration': 70, 'calories': 550, 'distance': None, 'days_ago': 1},
            {'user': thor, 'type': 'running', 'duration': 50, 'calories': 550, 'distance': 8.5, 'days_ago': 2},
            {'user': thor, 'type': 'cycling', 'duration': 80, 'calories': 650, 'distance': 22.0, 'days_ago': 3},
        ]
        
        # Create Activities - DC Team
        self.stdout.write('Creating DC activities...')
        dc_activities_data = [
            # Superman
            {'user': superman, 'type': 'running', 'duration': 70, 'calories': 800, 'distance': 12.0, 'days_ago': 1},
            {'user': superman, 'type': 'weightlifting', 'duration': 80, 'calories': 650, 'distance': None, 'days_ago': 2},
            {'user': superman, 'type': 'running', 'duration': 65, 'calories': 750, 'distance': 11.0, 'days_ago': 3},
            
            # Batman
            {'user': batman, 'type': 'weightlifting', 'duration': 75, 'calories': 550, 'distance': None, 'days_ago': 1},
            {'user': batman, 'type': 'running', 'duration': 55, 'calories': 600, 'distance': 9.0, 'days_ago': 1},
            {'user': batman, 'type': 'cycling', 'duration': 85, 'calories': 700, 'distance': 23.0, 'days_ago': 2},
            
            # Wonder Woman
            {'user': wonder_woman, 'type': 'weightlifting', 'duration': 65, 'calories': 500, 'distance': None, 'days_ago': 1},
            {'user': wonder_woman, 'type': 'running', 'duration': 50, 'calories': 550, 'distance': 8.5, 'days_ago': 2},
            {'user': wonder_woman, 'type': 'yoga', 'duration': 60, 'calories': 300, 'distance': None, 'days_ago': 3},
            
            # Flash
            {'user': flash, 'type': 'running', 'duration': 80, 'calories': 900, 'distance': 15.0, 'days_ago': 1},
            {'user': flash, 'type': 'running', 'duration': 75, 'calories': 850, 'distance': 14.0, 'days_ago': 2},
            {'user': flash, 'type': 'running', 'duration': 70, 'calories': 800, 'distance': 13.0, 'days_ago': 3},
            
            # Aquaman
            {'user': aquaman, 'type': 'swimming', 'duration': 60, 'calories': 650, 'distance': 3.0, 'days_ago': 1},
            {'user': aquaman, 'type': 'swimming', 'duration': 65, 'calories': 700, 'distance': 3.5, 'days_ago': 2},
            {'user': aquaman, 'type': 'weightlifting', 'duration': 55, 'calories': 450, 'distance': None, 'days_ago': 3},
        ]
        
        activities_data.extend(dc_activities_data)
        
        for activity_info in activities_data:
            Activity.objects.create(
                user=activity_info['user'],
                activity_type=activity_info['type'],
                duration=activity_info['duration'],
                calories=activity_info['calories'],
                distance=activity_info['distance'],
                date=date.today() - timedelta(days=activity_info['days_ago']),
                notes=f"Training session for {activity_info['user'].name}"
            )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        all_users = [iron_man, captain_america, black_widow, hulk, thor,
                     superman, batman, wonder_woman, flash, aquaman]
        
        for user in all_users:
            user_activities = Activity.objects.filter(user=user)
            total_calories = sum(activity.calories for activity in user_activities)
            total_duration = sum(activity.duration for activity in user_activities)
            total_count = user_activities.count()
            
            Leaderboard.objects.create(
                user=user,
                team=user.team,
                total_calories=total_calories,
                total_duration=total_duration,
                total_activities=total_count,
                period='all_time'
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts_data = [
            {
                'title': 'Superhero Cardio Blast',
                'description': 'High-intensity cardio workout to build endurance like a superhero',
                'activity_type': 'running',
                'difficulty': 'intermediate',
                'duration': 45,
                'calories_estimate': 500
            },
            {
                'title': 'Beginner Strength Training',
                'description': 'Basic strength training routine perfect for starting your hero journey',
                'activity_type': 'weightlifting',
                'difficulty': 'beginner',
                'duration': 30,
                'calories_estimate': 250
            },
            {
                'title': 'Advanced Power Lifting',
                'description': 'Intense powerlifting session for maximum strength gains',
                'activity_type': 'weightlifting',
                'difficulty': 'advanced',
                'duration': 90,
                'calories_estimate': 700
            },
            {
                'title': 'Speed Force Sprint Training',
                'description': 'Sprint intervals to build speed and agility like The Flash',
                'activity_type': 'running',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_estimate': 650
            },
            {
                'title': 'Aquatic Hero Swim',
                'description': 'Swimming workout for full-body conditioning',
                'activity_type': 'swimming',
                'difficulty': 'intermediate',
                'duration': 45,
                'calories_estimate': 450
            },
            {
                'title': 'Zen Warrior Yoga',
                'description': 'Relaxing yoga session for flexibility and mental clarity',
                'activity_type': 'yoga',
                'difficulty': 'beginner',
                'duration': 50,
                'calories_estimate': 200
            },
            {
                'title': 'Cycling Patrol Route',
                'description': 'Long-distance cycling for endurance building',
                'activity_type': 'cycling',
                'difficulty': 'intermediate',
                'duration': 75,
                'calories_estimate': 600
            },
            {
                'title': 'Hero Recovery Flow',
                'description': 'Gentle yoga flow for active recovery and injury prevention',
                'activity_type': 'yoga',
                'difficulty': 'beginner',
                'duration': 40,
                'calories_estimate': 180
            },
        ]
        
        for workout_info in workouts_data:
            Workout.objects.create(**workout_info)
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams created: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users created: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities created: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries created: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts created: {Workout.objects.count()}'))
        
        # Display top 5 leaderboard
        self.stdout.write('\n=== Top 5 Leaderboard ===')
        top_users = Leaderboard.objects.all().order_by('-total_calories')[:5]
        for entry in top_users:
            self.stdout.write(
                f'{entry.rank}. {entry.user.name} ({entry.team.name}) - '
                f'{entry.total_calories} calories, {entry.total_activities} activities'
            )
