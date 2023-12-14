from django.shortcuts import redirect, render
from .forms import RegistrationForm

def register(request, role):
  form = RegistrationForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('profile')
  # if request.method == 'POST':
  #   user_form = RegistrationForm(request.POST)
  #   profile_form = ProfileForm(request.POST)
  #     user_form.save()
  #     profile_form.save()
  #     print('Your account has been created')
  #     return redirect('login')
  # else:
  #   user_form = RegistrationForm()
  return render(request, "registration/register.html", {"form": form})

def profile(request):
  if not request.user.is_authenticated:
    return redirect('login')
  form = RegistrationForm(instance=request.user)
  return render(request, "profile.html", {'form': form})
