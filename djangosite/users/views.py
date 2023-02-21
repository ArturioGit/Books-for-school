from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserProfileUpdateForm


# Create your views here.
class CreateUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реєстрація'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизація'
        return context

    def get_success_url(self):
        return reverse_lazy('profile')


@login_required(login_url='/user/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'Профіль'
    }

    return render(request, 'users/profile.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')
