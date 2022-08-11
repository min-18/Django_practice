
from rest_framework import serializers
from .models import *

# 정참조로 하고 뷰에서 역참조조작

class UserSerializer(serializers.ModelSerializer):
    # 역참조 ; 여기 변수는 FK부분 related_name 이랑 같아야함.
    # rooms = RoomSerializer(many=True, read_only=True)
    # rooms = serializers.StringRelatedField(many=True)

    # user_create_rooms = serializers.SerializerMethodField()

    # get_(변수명)이어야 올바르게 작동한다.
    # def get_user_create_rooms(self, obj):
    #     room_list = []
    #     print(obj.rooms.room_title)
        # print(dir(obj))

        # for room in obj.room_set.all():
        #     room_list.append(room.room_title)
        # print(room_list)
        # return room_list


    class Meta:
        model = User
        fields = '__all__'      # 필요한 필드만 하고 싶을 땐 리스트 형태로 작성. ; fields = ['id', 'title']
        # fields = ['name', 'age', 'created'] 


class RoomSerializer(serializers.ModelSerializer):
    # user_id = serializers.StringRelatedField()
    
    # 유저 아이디값만,, 
    # user = UserSerializer

    # 유저 아이디랑 유저 객체정보까지 다!
    user_id = UserSerializer(read_only = True, many=True)    

    # user_id = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        # fields = [ 'room_title', 'user']
        fields = '__all__'
        # unique_together = ['user_id', 'room_title']






