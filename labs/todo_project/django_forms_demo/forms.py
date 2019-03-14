from django import forms

class CreateTask(forms.Form):
  # <label><input type="text" name="title" placeholder="add task title..."></label>
  title = forms.CharField(
    max_length=100,
    required=True,
    widget=forms.TextInput(
      attrs={
        'class' : 'form-control',
        'placeholder' : 'Enter a task name...',    
      }
    )
  )

  # <label><input type="date" name="due" required></label> -->
  due = forms.DateField()

