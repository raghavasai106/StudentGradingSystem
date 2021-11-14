# GradeSystem/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Grade, Course
from django.contrib.auth import get_user_model


# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'cell_phone')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'cell_phone')


class StudentGradingCreateForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request") # store value of request
        super(StudentGradingCreateForm, self).__init__(*args, **kwargs)
        self.fields['courseName'].queryset = Course.objects.filter(instructor=self.request.user)
        self.fields['student'].queryset = CustomUser.objects.filter(user_type='Student')


