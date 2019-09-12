from django.urls import path
# from .views import current_user , UserList , LoginAPIView
from core.views import LoginAPIView

urlpatterns = [
    # path('current_user/', current_user),
    # path('users/', UserList.as_view()),
    path('login', LoginAPIView.as_view())

]
