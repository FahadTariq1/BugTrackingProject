from rest_framework import serializers

class BugsSearchByProjectSerializer(serializers.Serializer):
    id =serializers.IntegerField()
    description = serializers.CharField()
    status = serializers.CharField()
    due_date = serializers.DateField()
    assigneduser = serializers.SerializerMethodField()

    def get_assigneduser(self, obj):
        return obj.assigneduser.name
    

class BugsCreationSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
    screenshot_type = serializers.CharField()
    due_date = serializers.DateField()
    assigneduser_id = serializers.IntegerField()
    assignedproject_id = serializers.IntegerField()

class BugsUpdateSerializer(serializers.Serializer):
    status = serializers.CharField()
