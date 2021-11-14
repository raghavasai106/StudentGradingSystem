from django.urls import path
from .views import SignUpView, GradeListView, StudentGradingCreateView, StudentGradingUpdateView, \
    StudentGradingDeleteView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create/', StudentGradingCreateView.as_view(), name='grade_create'),
    path('edit/<int:pk>/', StudentGradingUpdateView.as_view(), name='grade_edit'),
    path('delete/<int:pk>/', StudentGradingDeleteView.as_view(), name='grade_delete'),
    path('', GradeListView.as_view(), name='grade_list'),
]
