from django.contrib import admin
from .models import Question
from .models import Choices, UserProfile, LikeQuestion, Bookmarks
# Register your models here.

admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(UserProfile)
admin.site.register(LikeQuestion)
admin.site.register(Bookmarks)