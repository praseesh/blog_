from django.urls import path
from .views import UserRegistrationViews, UserLoginView, LogoutView

urlpatterns = [
    path('register/',UserRegistrationViews.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name="logout"),
]
