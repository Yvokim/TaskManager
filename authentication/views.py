from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms.forms import RegistrationForm
from authentication.models import Profile
from .forms.profileform import ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy
from django.urls import reverse


def home(request):
    return render(request, 'authentication/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')



    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


def profile_update(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'authentication/profile_update.html', {'form': form})


@login_required
def profile(request):
    profile = request.user.profile

    context = {
        'user': request.user,
        'profile': profile

    }
    return render(request, 'authentication/profile_display.html', context)


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def get_success_url(self):
        return reverse('home')


def logout_view(request):
    logout(request)
    return redirect('login')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('password_change_done')

    # def custom_password_change_view(request):
    # Use as_view() method to create a view function
    # return PasswordChangeView.as_view(
    # template_name='authentication/password_change.html',  # Custom template for password change form
    # success_url=reverse_lazy('password_change_done')       # Custom success URL
    # )(request)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'


class CustomPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'
