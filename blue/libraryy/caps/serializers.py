from rest_framework import serializers
from caps.models import User, Book

class UserSerializer(serializers.ModelSerializer):

     
    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "date_joined", "is_staff", "password"
        ]
    read_only_fields = ["password"]
    password = serializers.CharField(write_only=True)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id", "title", "price", "genre"
        ]
