from django.db import models

# class Room(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     room_title = models.TextField()
#     room_interest = models.CharField(max_length=10)
#     room_date = models.DateField(auto_now_add=True)
#     room_time = models.TimeField(auto_now_add=True)
#     room_place = models.CharField(max_length=50)
#     room_headcount = models.IntegerField()
#     room_status = models.IntegerField()
#     room_created_time = models.DateTimeField(auto_now_add=True)
#     applier1 = models.ForeignKey(User, on_delete=models.CASCADE)
#     applier2 = models.ForeignKey(User, on_delete=models.CASCADE)
#     applier3 = models.ForeignKey(User, on_delete=models.CASCADE)
#     applier4 = models.ForeignKey(User, on_delete=models.CASCADE)
#     applier5 = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.id} {self.room_title}"

# class Apply(models.Model):
#     user_id = models.For






class User(models.Model):
    name = models.CharField(max_length=5)
    age = models.IntegerField(default=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return str(self.id) + ". "+ self.name


class Room(models.Model):
    user_id = models.ForeignKey(User, related_name='rooms',on_delete=models.CASCADE,null=True)
    # user_id = models.ManyToManyField(User, verbose_name='유저')
    room_title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.room_title}"
