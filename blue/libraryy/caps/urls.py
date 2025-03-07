from django.urls import path
from caps.views import BookView, UserView, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('book/', BookView.as_view()),
    path('book/<int:id>/', BookView.as_view(), name='select_book_by_id'),
    path('user/', UserView.as_view()),
    path('user/<int:id>/', UserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),    
]
