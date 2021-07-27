from django.forms import ModelForm

from todo.models import Todo

class TodoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['completed'].widget.attrs = {
            'class': 'form-check'
        }
    class Meta:
        model = Todo
        fields = '__all__'
