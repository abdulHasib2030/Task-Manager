from django.shortcuts import render
from django.views.generic import FormView,View
from account.forms import *
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views import View
from django.shortcuts import redirect

########### User Registration ###########
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 
    
########### User Login ###############
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
########### User Logout ############
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('main-home')
    
########## User Profile Update View #########
class UserProfileUpdateView(View):
    template_name =   'accounts/profile.html'
    
    def get(self, request):
        form = UserProfileUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form':form})
    
########## User Change Password View #########
class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'    
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login')
    
