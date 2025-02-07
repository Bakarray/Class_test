from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import Http404
from .models import Task
from .forms import TaskForm, CustomUserCreationForm

# Create your views here.

# Task Creation view
class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'todo/create_task.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Task Reading view
class HomePageView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')
    

# Reading task description
class TaskDescriptionView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todo/task_desc.html"
    context_object_name = "task"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("Task does not exist")
        return obj

# Task Updating view
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todo/edit_task.html'
    context_object_name = "task"
    form_class = TaskForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("Task does not exist")
        return obj

# Task Deleting view
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home_page')
    template_name = 'todo/delete_task.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("Task does not exist")
        return obj

# User signup view
class SignupView(CreateView, SuccessMessageMixin):
    form_class = CustomUserCreationForm
    template_name = 'todo/auth.html'
    success_url = reverse_lazy('login')
    success_message = "Signup successful! You can log in now."
    extra_context = {'page': "signup"}

    def form_valid(self, form):
        form.instance.username = form.instance.username.lower()
        return super().form_valid(form)


# User login view
class CustomLoginView(LoginView):
    template_name = 'todo/auth.html'
    next_page = 'home_page'


# User logout view
class CustomLogoutView(LogoutView):
    next_page = 'login'
