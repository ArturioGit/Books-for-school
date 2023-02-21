from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *


class CourseHome(DataMixin, ListView):
    template_name = 'course/index.html'
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_selected'] = 0
        context['subject_selected'] = 'all'
        context['title'] = 'Шкільні курси'
        return context

    def get_queryset(self):
        return Book.objects.filter(is_published=True)


class CourseDetails(DataMixin, DetailView):
    template_name = 'course/details.html'
    slug_url_kwarg = 'course_slug'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['course'].title
        context['class_selected'] = context['course'].group.number
        context['subject_selected'] = context['course'].subject.slug
        return context


class CourseByCategories(DataMixin, ListView):
    template_name = 'course/index.html'
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_selected'] = self.kwargs['group_number']
        context['subject_selected'] = self.kwargs['subject_slug']
        context['title'] = 'Шкільні курси'
        context['len_courses'] = len(context['courses'])
        return context

    def get_queryset(self):
        group_number = self.kwargs['group_number']
        subject_slug = self.kwargs['subject_slug']
        if group_number != 0:
            group = get_object_or_404(Group, number=group_number)
            group_number = group.number

        if subject_slug != 'all':
            subject = get_object_or_404(Subject, slug=subject_slug)
            subject_slug = subject.slug

        if group_number == 0:
            if subject_slug == 'all':
                courses = Book.objects.order_by('group', 'title')
            else:
                courses = Book.objects.filter(subject_id=subject.id).order_by('group', 'title')
        else:
            if subject_slug == 'all':
                courses = Book.objects.filter(group_id=group.id).order_by('title')
            else:
                courses = Book.objects.filter(group_id=group.id).filter(subject_id=subject.id).order_by('title')

        return courses.filter(is_published=True)


class CourseAddBook(LoginRequiredMixin, CreateView):
    form_class = AddBookForm
    template_name = 'course/add_book.html'
    login_url = '/user/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додати підручник'
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1 style='text-align:center;font-size:100px;'>Page not found</h1>")
