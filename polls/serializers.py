from rest_framework import serializers
from .models import Poll

class PollsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Poll
    fields = '__all__'
    read_only_fields = ('created_at',)