from rest_framework import serializers

from watchlist_app.models import Movie

def name_length(value):
    if value < 2:
        raise serializers.ValidationError("Name too short")

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        """
               Create and return a new `Movie` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
               Update and return an existing `Movie` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name too short")
    #     else:
    #         return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different!")
        else:
            return data