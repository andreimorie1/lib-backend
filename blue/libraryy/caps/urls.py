from django.urls import path
from caps.views import BookView, UserView, RegisterView

urlpatterns = [
    path('book/', BookView.as_view()),
    path('user/', UserView.as_view()),
    path('Register/', RegisterView.as_view()),
]
