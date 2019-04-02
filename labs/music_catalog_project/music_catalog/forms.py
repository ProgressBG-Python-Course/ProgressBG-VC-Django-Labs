from django import forms

class FormArtist(forms.Form):
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