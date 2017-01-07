from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from simplemooc.core.utils import generate_hash_key
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


def register(request):
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = { 'form': form }
    return render(request, template_name, context)


def password_reset(request):
    template_name = 'accounts/password-reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(email=form.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'accounts/edit-password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)