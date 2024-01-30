from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from posting.models import Resume, Posting
from posting.forms import ResumeForm

def register(request, role):
  form = RegistrationForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('profile')
  return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
  return render(request, "profile/profile.html")

@login_required
def edit_profile(request):
  form = RegistrationForm(instance=request.user)
  return render(request, "profile/edit_profile.html", {'form': form})

@login_required
def resumes(request):
  if request.method == "POST":
    form = ResumeForm(request.POST, request.FILES)
    form.instance.user_id = request.user
    if form.is_valid():
      form.save()
      return redirect('resumes')
  resumes = Resume.objects.filter(user_id=request.user)
  form = ResumeForm()
  return render(request, "profile/resumes.html", {"resumes": resumes, "form": form})

@login_required
def postings(request):
  postings = Posting.objects.filter(owner=request.user)
  return render(request, "profile/postings.html", {"postings": postings})