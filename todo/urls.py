from django.urls import path, re_path
from .views import (TodoCreateApiView, TodoDeleteApiView,
                    TodoListApiView, UpdateApiView, todo_view)
urlpatterns = [
    path('', todo_view, name="home"),

    path(r'api/create', TodoCreateApiView.as_view(),
         name="createapi"),
    path(r'api/delete/<int:pk>', TodoDeleteApiView.as_view(),
         name="deleteapi"),
    re_path('^api/list(?P<id>)/$', TodoListApiView.as_view(),
            name="listapi"),
    path(r'api/update/<int:pk>', UpdateApiView.as_view(),
         name="updateapi"),
]
