from rest_framework import serializers
from bugs.models import Bug


class ProjectDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    projectname = serializers.CharField()
    description = serializers.CharField()
    total_bugs = serializers.SerializerMethodField()
    closed_bugs = serializers.SerializerMethodField()

    def get_total_bugs(self, obj):
        return Bug.objects.filter(assignedproject=obj).count()

    def get_closed_bugs(self, obj):
        return Bug.objects.filter(assignedproject=obj, bug_type='closed').count()

class ProjectCreationSerializer(serializers.Serializer):
    projectname = serializers.CharField()
    description = serializers.CharField()
    manager_id = serializers.IntegerField() 


