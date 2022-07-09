from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# admin 페이지에서 보이도록
admin.site.register(Question)
admin.site.register(Choice)
