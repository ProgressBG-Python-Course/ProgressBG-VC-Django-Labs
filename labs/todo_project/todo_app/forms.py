from django import forms 
from django.utils.timezone import make_aware
from django.utils import timezone
import datetime
import re

due_date_format = "%Y-%m-%dT%H:%M" #  2019-04-10T01:00

# The HTML Form:
# <form action="{% url 'todo_add' %}" method="POST">
#   {% csrf_token %}
#   <input type="text" name="task_title" placeholder="please, enter a task title...">
#   <button type="submit">Add</button>  
# </form>

def days_from_now_1():  
  return timezone.now() + timezone.timedelta(days=1)

class CreateUpdateTaskForm(forms.Form):
  # add input field for title = models.CharField('Title', max_length=100)
  title = forms.CharField(
    max_length=100,
    required=True, 
    help_text="Enter a Task Title",
    widget=forms.TextInput(
      attrs={
        'class' : 'form-control', 
        'placeholder' : 'Enter todo title...', 
      }
    )    
  )
  
  image = forms.ImageField(required=False)

  description = forms.CharField(    
    required=False,
    help_text="Enter a Task Description",
    widget=forms.Textarea(
      attrs={
        'class' : 'form-control', 
        'placeholder' : 'description...', 
      }
    )    
  )

  due = forms.DateTimeField(
    initial=days_from_now_1,
    help_text="Task Due (default - 1 day from now)",
    widget = forms.DateTimeInput(
      attrs={'type': 'datetime-local', 'class': 'form-control'},
      format= due_date_format
    ),
    input_formats = [due_date_format,]
  )


  def clean_title(self):
    title = self.cleaned_data.get('title', None)        

    # TODO: multiple errors per field
    # DONE: https://docs.djangoproject.com/en/2.2/ref/forms/validation/#raising-multiple-errors
    errors_list = [];
    if (not re.match( r'^[A-z]', title)):
      e1 = forms.ValidationError("title must start with letter")
      errors_list.append(e1)

    if len(title) < 3:
      e2 = forms.ValidationError("title must be 3 or more symbols")
      errors_list.append(e2)

    if errors_list:
      raise forms.ValidationError(errors_list)
        

    # always return the cleaned data
    return title

  def clean_due(self):
    # clean the data:
    data = self.cleaned_data.get('due')

    # Check if a date is not in the past.
    now = make_aware(datetime.datetime.now())

    if data < now:
      raise forms.ValidationError('Invalid date - due date is in past')


    # always return the cleaned data.
    return data


