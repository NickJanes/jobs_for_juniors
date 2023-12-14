from django import forms
from .models import Posting
 
 
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