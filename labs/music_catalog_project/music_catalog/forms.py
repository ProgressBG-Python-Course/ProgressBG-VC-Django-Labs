from django import forms
from .models import Artist

class FormArtist_DjangoForm(forms.Form):
  name = forms.CharField(
    max_length=50,
    required=True,
    widget=forms.TextInput(
      attrs={
        'class' : 'form-control',
        'placeholder' : 'Enter an artist name...',
      }
    )
  )

  about = forms.CharField(
    widget=forms.Textarea(
      attrs = {
        'placeholder': 'About Artist'
      }
    )
  )


class FormArtist(forms.ModelForm):
  class Meta:
    model = Artist
    # fields = ['pub_date', 'headline', 'content', 'reporter']
    exclude = ['id']

    # TODO: make it work as is
    # DONE: CharField => forms.TextInput
    widgets = {
      'name': forms.TextInput(
        attrs={
          'class' : 'form-control',
          'placeholder' : 'Enter an artist name...',
        }
      )
    }
