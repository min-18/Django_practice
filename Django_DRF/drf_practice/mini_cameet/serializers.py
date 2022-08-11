
from rest_framework import serializers
from .models import *
from .userserializers import *

class UserSerializer(serializers.ModelSerializer):
    # 역참조 ; 여기 변수는 FK부분 related_name 이랑 같아야함.
    # rooms = RoomSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'      # 필요한 필드만 하고 싶을 땐 리스트 형태로 작성. ; fields = ['id', 'title']
        # fields = ['name', 'age', 'created']


class RoomSerializer(serializers.ModelSerializer):
    # user_id = serializers.StringRelatedField()

    # user_id = UserSerializer(source='user_set', read_only=True)
    user_id = UserSerializer

    class Meta:
        model = Room
        # fields = [ 'room_title', 'user']
        fields = '__all__'
        # unique_together = ['user_id', 'room_title']


    
