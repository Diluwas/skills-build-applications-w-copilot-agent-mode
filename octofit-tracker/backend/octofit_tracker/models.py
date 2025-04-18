from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 24
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if not isinstance(value, ObjectId):
            return ObjectId(value)
        return value

    def to_python(self, value):
        if not isinstance(value, ObjectId):
            return ObjectId(value)
        return value

class User(models.Model):
    _id = ObjectIdField(primary_key=True, default=ObjectId)  # Custom ObjectIdField for MongoDB compatibility
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords in production
    name = models.CharField(max_length=255, null=True, blank=True)  # Optional field for full name

class Team(models.Model):
    _id = ObjectIdField(primary_key=True, default=ObjectId)  # Custom ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True, default=ObjectId)  # Custom ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)  # Align with test data
    duration = models.DurationField()  # Align with test data
    description = models.TextField(null=True, blank=True)  # Optional field for additional details
    date = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True, default=ObjectId)  # Custom ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Align with test data
    score = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True, default=ObjectId)  # Custom ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=255)  # Align with test data
    description = models.TextField()  # Align with test data
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()