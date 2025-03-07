from rest_framework import serializers
from caps.models import User, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "date_joined", "is_staff", "password"
        ]
     
    def create(self, validated_data):
        # Get the is_superuser value to determine user type
        is_staff = validated_data['is_staff']

        # Check if the user should be a superuser or a regular user
        if is_staff:
            # Create a superuser (admin)
            user = User.objects.create_superuser(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
        else:
            # Create a regular user (non-admin)
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
        
        return user

    
    read_only_fields = [
        "id", "date_joined", "is_staff"
        ]
    
    #hide fields
    password = serializers.CharField(write_only=True)
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id", "title", "price", "genre"
        ]
        