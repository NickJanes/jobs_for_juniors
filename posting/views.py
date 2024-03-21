from django.shortcuts import render, redirect
from django.forms import ModelChoiceField
from .models import Posting, PostingTag, Resume, Tag
from .forms import PostingForm

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
  posting = Posting.objects.get(id=posting_id)
  return render(request, 'posting-detailed.html', {'posting': posting})

def create_posting(request):
  if not request.user.is_authenticated:
    return redirect('/accounts/login/')

  posting_form = PostingForm(request.POST or None)
  if posting_form.is_valid():
    posting = posting_form.save(commit=False)
    posting.owner = request.user
    posting.save()
    return redirect('/posting/' + str(posting.id))

  return render(request, 'create_posting.html', {"form": posting_form})

def apply(request, posting_id):
  if not request.user.is_authenticated:
    return redirect('/accounts/login/?next=../../apply/{}'.format(posting_id))
  
  resumes = Resume.objects.filter(user_id=request.user).all()
  if len(resumes) == 0:
    return redirect('/accounts/profile/resumes/?next=../../apply/{}'.format(posting_id))
                    
  posting = Posting.objects.get(id=posting_id)
  return render(request, 'apply.html', {"resumes": resumes, "posting": posting})

def delete(request, posting_id):
  if not request.user.is_authenticated:
    return redirect('/')
  
  posting = Posting.objects.get(id=posting_id)
  if posting.owner == request.user:
    posting.delete()
  return redirect('/')