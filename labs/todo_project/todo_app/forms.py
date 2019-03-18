from django import forms 

# The HTML Form:
# <form action="{% url 'todo_add' %}" method="POST">
#   {% csrf_token %}
#   <input type="text" name="task_title" placeholder="please, enter a task title...">
#   <button type="submit">Add</button>  
# </form>

class CreateUpdateTaskForm(forms.Form):
  # add input field for title = models.CharField('Title', max_length=100)
  title = forms.CharField(
    max_length=100,
    required=True, 
    widget=forms.TextInput(
      attrs={
        'class' : 'form-control', 
        'placeholder' : 'Enter todo title...', 
      }
    )
  )

  description = forms.CharField(    
    required=False,
    widget=forms.Textarea(
      attrs={
        'class' : 'form-control', 
        'placeholder' : 'description...', 
      }
    )    
  )


  # due = forms.DateTimeInput(format="%d %b %Y %H:%M:%S %Z")
  due = forms.DateTimeField(
    required=False, 
    widget = forms.DateInput(
      attrs={'type': 'date', 'class': 'form-control'}
    )
  )

