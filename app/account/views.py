from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth import logout
from django.urls import reverse_lazy

# decoradores
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserLoginView(LoginView):
  template_name = 'account/login.html'
  form_class = LoginForm

  def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('account:dashboard'))  # Redirige al dashboard si el usuario ya está autenticado
        return super().dispatch(request, *args, **kwargs)

@login_required
def dashboard(request):
  return render(request,'account/dashboard.html',{'section': 'DASHBOARD'})

@login_required
def logout_view(request):
  logout(request)
  return redirect('/account/login/')