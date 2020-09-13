from .models import Todo
from django.shortcuts import render
from .forms import TodoForm
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from .serializer import TodoSerializer, TodoUpdateSerializer


class TodoCreateApiView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDeleteApiView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateApiView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoUpdateSerializer


class TodoListApiView(ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self, *args, **kwargs):
        return Todo.objects.filter(author__id=self.request.GET.get('id'))


def todo_view(request):

    if not request.user.is_authenticated:
        print("not logged in")
        return render(request, 'index.html')
    objects = Todo.objects.filter(author=request.user)
    if request.method == "POST" and 'text' in request.POST:
        form = TodoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
    elif request.method == "POST" and 'pk' in request.POST:
        pk = request.POST.get("pk")
        Todo.objects.get(pk=pk).delete()
        form = TodoForm()
    else:
        form = TodoForm()

    return render(request, 'index.html', {"todos": objects, "todoform": form})
