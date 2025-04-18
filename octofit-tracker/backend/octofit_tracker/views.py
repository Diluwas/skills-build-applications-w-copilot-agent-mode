from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(["GET"])
def api_root(request, format=None):
    codespace_url = "https://shiny-space-happiness-6wjqvpgw4gqc4xrj-8000.app.github.dev"
    return Response({
        "users": f"{codespace_url}/api/users/",
        "teams": f"{codespace_url}/api/teams/",
        "activity": f"{codespace_url}/api/activity/",
        "leaderboard": f"{codespace_url}/api/leaderboard/",
        "workouts": f"{codespace_url}/api/workouts/",
    })