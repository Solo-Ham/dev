from django import forms
from .models import Question, Choices, UserProfile

class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','question_text', 'image']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Choices
        fields = ['choice_text']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
