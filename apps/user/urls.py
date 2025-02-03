
from django.urls import path
from .views import *
urlpatterns = [
    path("register/", UserRegister.as_view(),name = 'user registrations'),
    path("login/", UserLogin.as_view(),name = 'user login'),
    path("logout/", UserLogOut.as_view(),name = 'user logout'),
    path("profile/", UserProfile.as_view(),name = 'user profile'),
    path("profile/edit/", UserProfileEdit.as_view(),name = 'user profile Edit'),
    path("order/", UserOrder.as_view(),name = 'user UserOrder'),
    path("order/single/<int:o_id>/", UserSingleOrder.as_view(),name = 'user UserSingleOrder'),
]
