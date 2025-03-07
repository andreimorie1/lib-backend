from caps.models import Book, User
from rest_framework_simplejwt.tokens import RefreshToken, Token
from caps.serializers import BookSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 
from rest_framework import status
from caps.permissions import IsAdminOrReadOnly
# Create your views here.

class BookView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    
    def get(self, request, id=None):
        if id is None:
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
        else:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
 
        book.delete()
        return Response({
            "Success Message" : "deleted"
            },status=status.HTTP_204_NO_CONTENT)
    
class UserView(APIView):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
        
    def post (self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data, partial=True)
        except:
            return Response({
                "Error Message " : " User cannot be found"
            }, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except:
            return Response({
                "Error Message " : " User cannot be found"
            }, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({
            "Success Message ": "Data deleted rawr!"
            }, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post (self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        confirm_password = request.data["confirm_password"]
        
        user = authenticate(username=username, password=password)
        
        if password != confirm_password:
            return Response({"detail" : "Password do not match"}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        return Response(
            {
            "access": str(access_token),
            "refresh": str(refresh)

        }, status=status.HTTP_202_ACCEPTED
        )

        
        
        
        
        
        
    
    
