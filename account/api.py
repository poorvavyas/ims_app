from django.contrib.auth.models import User as user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, View
from django.views import View
from account.form import user_form, login_form
from django.contrib.auth import authenticate, login, logout


def logout_user(request):
    logout(request)
    return redirect('home')


class LoginUser(View):
    model = user_model
    form_class = login_form.LoginForm
    template_name = 'user/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print('invalid login')
        return redirect(reverse('incident_list', kwargs={}))


class AddUser(CreateView):
    model = user_model
    form_class = user_form.UserForm
    template_name = 'user/add_user.html'

    def get_success_url(self):
        return reverse('login_user', kwargs={})