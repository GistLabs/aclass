from rest_framework import serializers
from .sanitizer import sanitize
from .models import Todo


class TitleField(serializers.CharField):
    def get_attribute(self, instance):
        raw_text = super().get_attribute(instance)
        return sanitize(raw_text)

    def to_representation(self, value):
        return super().to_representation(value)


class TodoSerializer(serializers.ModelSerializer):

    title = TitleField()

    class Meta:
        
        model = Todo
        fields = ('id', 'title', 'description', 'priority', 'completed')
