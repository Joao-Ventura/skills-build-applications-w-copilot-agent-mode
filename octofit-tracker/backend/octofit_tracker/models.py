from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.EmailField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.EmailField()
    points = models.IntegerField()

class Workout(models.Model):
    user = models.EmailField()
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
