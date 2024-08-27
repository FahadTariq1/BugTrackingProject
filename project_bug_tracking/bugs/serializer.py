from company_users.models import CompanyUser
from rest_framework import serializers

class BugsSearchByProjectSerializer(serializers.Serializer):

    description = serializers.CharField()
    bug_type = serializers.CharField()
    due_date = serializers.DateField()
    assigneduser = serializers.SerializerMethodField()

    def get_assigneduser(self, obj):
        return obj.assigneduser.username
    

class BugsCreationSerializer(serializers.Serializer):
    
    title = serializers.CharField()
    description = serializers.CharField()
    bug_type = serializers.CharField()
    screenshot_type = serializers.CharField()
    due_date = serializers.DateField()
    assigneduser = serializers.SerializerMethodField()

class BugsUpdateSerializer(serializers.Serializer):
    bug_type = serializers.CharField()