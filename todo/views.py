from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import ToDoItem
# Create your views here.

def todoView(request):
    all_items = ToDoItem.objects.all()
    return render(request,'todo.html', {'all_items' : all_items})

def addTodo(request):
    #create a new todo item
    #redirect to /todo/

    content_request = request.POST['content']
    new_item = ToDoItem(content=content_request)
    new_item.save()
    return HttpResponseRedirect('/todo')

def deleteTodo(request, id):
    #delete a new todo item
    #redirect to /todo/
    item = ToDoItem.objects.get(id=id)
    item.delete()

    return HttpResponseRedirect('/todo')