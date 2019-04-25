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
    required=False,
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
        
    widgets = {
      'name': forms.TextInput(
        attrs={
          'class' : 'form-control',
          'placeholder' : 'Enter an artist name...',
        }
      )
    }

  def is_valid(self):
    print(f"self: {self}")    
    is_valid = super(FormArtist, self).is_valid()    
    if not is_valid:
      print("###########################")
      print(f"self.errors: {self.errors}")
      for field in self.errors.keys():
        print("ValidationError: {}{} : {}{}".format(
            type(self),
            field,
            self.data[field],
            self.errors[field].as_text()
          )
        )
    return is_valid
