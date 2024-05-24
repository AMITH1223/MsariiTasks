from rest_framework import serializers
from .models import Task, UserData, StudyGroup, CommunityForum

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'item', 'person', 'status', 'start_date', 'end_date', 'tags','autotimeline']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id','name', 'email', 'interests', 'activitylog', 'interaction']

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ['id', 'user_data',  'description', 'topic_category']


class CommunityForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityForum
        fields = ['id', 'user_data', 'description', 'topic_category']