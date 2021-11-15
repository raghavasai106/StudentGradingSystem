from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, StudentGradingCreateForm
from .models import Grade
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.core.mail import send_mail
# send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'grade_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Grades = Grade.objects.all()
        if self.request.user.user_type == "Student":
            Grades = Grades.filter(student=self.request.user)
        else:
            Grades = Grades.filter(courseName__in=self.request.user.course_set.all())

        context['grades'] = Grades
        # context['available_rooms'] = Rooms.objects.filter(assigned=False).count()
        return context



class StudentGradingCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    template_name = 'grade_create.html'
    success_url = reverse_lazy('grade_list')
    form_class = StudentGradingCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class StudentGradingUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    template_name = 'grade_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('grade_list')


class StudentGradingDeleteView(DeleteView):
    model = Grade
    template_name = 'grade_delete.html'
    success_url = reverse_lazy('grade_list')



class ChangePwView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/change_pw.html'

class PwResetView(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('pw_reset_done')
    template_name = 'registration/pw_reset.html'

class PwResetDoneView(PasswordResetDoneView):
    template_name = 'registration/pw_reset_done.html'

class PwResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('pw_reset_complete')
    template_name = 'registration/pw_reset_confirm.html'

class PwResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/pw_reset_complete.html'
