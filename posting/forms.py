from django import forms
from .models import Posting, Application, Resume
 
 
# creating a form
class PostingForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Posting
 
        # # specify fields to be used
        # fields = [
        #     "title",
        #     "description",
        # ]
        exclude = ['owner']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'file']