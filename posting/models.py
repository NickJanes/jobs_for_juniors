from django.db import models
from users.models import User

class Posting(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.CharField(max_length=10000)
  salary_low = models.IntegerField()
  salary_high = models.IntegerField()
  flexibility = models.CharField(max_length=1, choices=(("O", "Onsite"), ("H", "Hybrid"), ("R", "Remote")), default="O")

  def _get_tags(self):
    return [str(x) for x in PostingTag.objects.filter(posting__pk=self.pk)]
  _get_tags.short_description = 'tags'

  def __str__(self):
    return self.title + " - " + self.company

class Tag(models.Model):
  name = models.CharField(max_length=32, unique=True)

  def __str__(self):
    return self.name

class PostingTag(models.Model):
  posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.tag)
  
  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['posting', 'tag'], name='unique_tag_post')
    ]


class Resume(models.Model):

  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.TextField(max_length=100)
  file = models.FileField(upload_to="files/resumes")

class Application(models.Model):
  posting_id = models.ForeignKey(Posting, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  resume_id = models.ForeignKey(Resume, on_delete=models.CASCADE)