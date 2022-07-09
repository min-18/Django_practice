from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.index ),
    # int형인 question_id를 넘겨줌.
    path('<int:question_id>/',views.detail, name='detail' ),


]