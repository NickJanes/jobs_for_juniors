from django.shortcuts import render, redirect
from django.forms import ModelChoiceField
from .models import Posting, PostingTag, Tag
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
  return render(request, 'posting.html', vars(Posting.objects.get(id=posting_id)))

def create_posting(request):
  if not request.user.is_authenticated:
    return redirect('accounts/login/')

  posting_form = PostingForm(request.POST or None)
  if posting_form.is_valid():
    posting = posting_form.save(commit=False)
    posting.owner = request.user
    posting.save()
    return redirect('posting/' + str(posting.id))

  return render(request, 'create_posting.html', {"form": posting_form})
