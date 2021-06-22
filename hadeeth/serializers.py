from rest_framework import serializers
from .models import Hadeeth

class HadeethSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hadeeth
        fields = ('id', 'content', 'book', 'narrator', 'uploaded_by')
