from django import forms 

# The HTML Form:
# <form action="create_task" method="POST">
#   {% csrf_token %}
#   <label><input type="text" name="title" placeholder="add task title..."></label>
#   <label><input type="date" name="due" placeholder="add task title..."></label>
#   <button>Add</button>
# </form>

class CreateTaskForm(forms.Form):
  # add input field for title = models.CharField('Title', max_length=100)
  title = forms.CharField(
    max_length=100,
    required=True, 
    widget=forms.TextInput(
      attrs={
        'class' : 'form-control', 
        'placeholder' : 'Enter todo e.g. Delete junk files', 
      }
    )
  )

  # due = forms.DateTimeInput(format="%d %b %Y %H:%M:%S %Z")
  due = forms.DateTimeField(
      widget = forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'})
  )


class UpdateTaskForm(CreateTaskForm):
  description = forms.CharField(    
    required=False,
    widget=forms.Textarea
  )    


