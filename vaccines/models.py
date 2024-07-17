from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    school_attended = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)

class Question(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    question_text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_pics/',height_field=None, width_field=None, max_length=None, null=True, blank=True)
    #user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    #owner_profile = models.OneToOneField(UserProfile, null=True, blank=True)

    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ['-updated_at', '-pub_date']


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)
    answer_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    answer_date = models.DateTimeField(auto_now_add=True)
    answer_update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.choice_text


    class Meta:
        ordering = ['-answer_date', '-answer_update']


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pics/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
#     school_attended = models.CharField(max_length=200, null=True, blank=True)
#     occupation = models.CharField(max_length=200, null=True, blank=True)
#     bio = models.CharField(max_length=300, null=True, blank=True)
    

class LikeQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='likes')


class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-time_updated', 'time_created']