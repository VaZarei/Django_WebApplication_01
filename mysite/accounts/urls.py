from django.urls import path
from .views import AccountsUserCreationForm




urlpatterns = [
    path('newregister/',AccountsUserCreationForm.as_view(), name="AccountsUserCreationForm_url" )
]
