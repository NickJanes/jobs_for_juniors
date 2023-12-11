from django.shortcuts import render, redirect
from .models import Posting, PostingTag, Tag
from .forms import RegistrationForm, ProfileForm

# Create your views here.
def index(request):
  tag_filter = request.GET.get('tag')
  if tag_filter:
    tag = Tag.objects.get(name__iexact=tag_filter)
    postings = Posting.objects.all()
    # print(PostingTag.objects.filter(tag__pk=tag.id))
    postings = [x.posting for x in PostingTag.objects.filter(tag__pk=tag.id)]
  else:
    postings = Posting.objects.all()

  for posting in postings:
    posting.tags = PostingTag.objects.filter(posting__title=posting.title)

  context = {"postings": postings}
  # context = Posting.object.all()
  return render(request, 'index.html', context)

def posting(request, posting_id):
  return render(request, 'posting.html', vars(Posting.objects.get(id=posting_id)))

def create_posting_form(request):

  return render(request, 'create_posting_form.html')

def create_posting_action(request):
  title = request.POST.get("title", "")
  company = request.POST.get("company", "")
  description = request.POST.get("description", "")
  low = request.POST.get("salary_low", "")
  high = request.POST.get("salary_high", "")
  flexi = request.POST.get("flexibility", "")
  if title != "" and company != "" and description != "" and low != "" and high != "" and flexi != "":
    Posting.objects.create(title=title, company=company, description=description, salary_low=low, salary_high=high, flexibility=flexi).save()
  return render(request, 'create_posting_action.html')

def register(request):
  if request.method == 'POST':
    user_form = RegistrationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      print('Your account has been created')
      return redirect('login')
  else:
    user_form = RegistrationForm()
    profile_form = ProfileForm()
  return render(request, "registration/register.html", {'user_form': user_form, 'profile_form': profile_form})

def profile(request):
  if not request.user.is_authenticated:
    return redirect('login')
  
  context = {"Success": True}
  try:
    user = request.user
    user.profile.role = request.POST.get("role")
    # request.user.username = request.POST.get("username")
    # request.user.save()
    request.profile.save()
  except:
    print("FAILED")
    context['Success'] = False
  return render(request, "profile.html", context)
