from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template.response import TemplateResponse

from todo.models import Todo


# Create your views here.
class TodoListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'todo_list': Todo.objects.all()
        }
        return TemplateResponse(request, 'todo_list.html', context)


class TodoAddView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'todo_add.html', {})

    def post(self, request, *args, **kwargs):
        description = request.POST['description']
        Todo.objects.create(description=description)
        return HttpResponseRedirect('/')


class TodoDoneView(View):
    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['todo_id'])
        todo.is_done = True
        todo.save()
        return HttpResponseRedirect('/')
