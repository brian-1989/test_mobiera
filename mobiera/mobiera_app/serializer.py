from rest_framework import serializers

class ConcatenateWordsSerializer(serializers.Serializer):
    word_lists = serializers.ListField()
