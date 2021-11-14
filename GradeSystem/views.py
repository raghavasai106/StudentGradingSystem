from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, StudentGradingCreateForm
from .models import Grade


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


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


class StudentGradingUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    template_name = 'grade_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('grade_list')


class StudentGradingDeleteView(DeleteView):
    model = Grade
    template_name = 'grade_delete.html'
    success_url = reverse_lazy('grade_list')
