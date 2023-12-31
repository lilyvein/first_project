from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, UpdateView, DeleteView, )
from django.urls import reverse_lazy
from.models import Student, Teacher, Subject


# Create your views here.
class MyHomeView(TemplateView):
    template_name = 'first_app/home.html'


class StudentListView(ListView):
    # model_list.html -> student_ist.html
    model = Student  # Connected to Models Student
    queryset = Student.objects.order_by('name')  # Result ordered by name
    context_object_name = 'students'  # default object_list now students
    paginate_by = 10  # 10 per page in ListView


class StudentDetailView(DetailView):
    # Return only one model entry
    # default template model_detail.html => student_detail.html
    model = Student


class StudentCreateView(CreateView):
    template_name = 'first_app/student_form_create.html'
    model = Student
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('first_app:student_list')


class StudentUpdateView(UpdateView):
    # model_form.html => student_form.html
    model = Student
    fields = ['name', 'weight']  # update only this fields
    success_url = reverse_lazy('first_app:student_list')


class StudentDeleteView(DeleteView):
    # Form -> Confirm Delete Button
    # default template name => model_confirm_delete.html ->
    # -> student_confirm_delete.html
    model = Student
    # redirect after successful delete
    success_url = reverse_lazy('first_app:student_list')


class TeacherListView(ListView):

    model = Teacher  # Connected to Models Teacher
    queryset = Teacher.objects.order_by('name')  # Result ordered by name
    context_object_name = 'teacher'  # default object_list now teacher
    # paginate_by = 10  # 10 per page in ListView


class TeacherCreateView(CreateView):
    template_name = 'first_app/teacher_form_create.html'
    model = Teacher
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('first_app:teacher_list')


class SubjectListView(ListView):
    model = Subject
    queryset = Subject.objects.order_by('subject')  # Result ordered by name
    context_object_name = 'subject'  # default object_list now teacher


class SubjectCreateView(CreateView):
    template_name = 'first_app/subject_form_create.html'
    model = Subject
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('first_app:subject_list')


class SubjectDetailView(DetailView):
    model = Subject


class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['subject']  # update only this fields
    success_url = reverse_lazy('first_app:subject_list')


class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('first_app:subject_list')
