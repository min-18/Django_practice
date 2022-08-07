from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from mini_cameet import views


urlpatterns = [
    path('user/', views.UserListCreateAPIView.as_view()),
    path('room/', views.RoomListCreateAPIView.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)