from django.urls import path
from .views import SignUpView, GradeListView, StudentGradingCreateView, StudentGradingUpdateView, \
    StudentGradingDeleteView, ChangePwView, PwResetView, PwResetDoneView, PwResetConfirmView, PwResetCompleteView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create/', StudentGradingCreateView.as_view(), name='grade_create'),
    path('edit/<int:pk>/', StudentGradingUpdateView.as_view(), name='grade_edit'),
    path('delete/<int:pk>/', StudentGradingDeleteView.as_view(), name='grade_delete'),
    path('', GradeListView.as_view(), name='grade_list'),
    # path('change-password/', ChangePwView.as_view(), name='change_pw'),
    # path('password-reset/', PwResetView.as_view(), name='pw_reset'),
    # path('password-reset/done/', PwResetDoneView.as_view(), name='pw_reset_done'),
    # path('reset/<uidb64>/<token>/', PwResetConfirmView.as_view(), name='pw_reset_confirm'),
    # path('reset/done/', PwResetCompleteView.as_view(), name='pw_reset_complete'),
]

#User URL Configuration





