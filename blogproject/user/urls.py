from django.urls import path
from .views import UserRegistrationViews, UserLoginView, LogoutView, UserListView

urlpatterns = [
    path('register/',UserRegistrationViews.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('users/', UserListView.as_view(), name='user-list'),
    # path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
]
