from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics


# GenericAPIView + Mixin
# 
class UserListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoomListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Room.objects.all()
    # queryset = Room.user_id.user_set.all()
    
    # 역참조할 때는 호스트가 만든 여러개의 방을 보여줘야 하니 (many=True)를 덧붙여줘야한다.
    # 반대로 정참조일 때는 룸에서 호스트(유저) 한명에 대한 정보만 가져오면 되니 (many=True) 없이 써줘야 한다.
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
