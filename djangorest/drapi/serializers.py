from rest_framework import serializers

class AiSerializer(serializers.Serializer):
    tname = serializers.CharField(max_length=20)
    course_name = serializers.CharField(max_length=20)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()