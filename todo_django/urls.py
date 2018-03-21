from django.contrib import admin
from django.urls import include, path

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('add/', views.TodoAddView.as_view(), name='todo-add'),
    path(
        'done/<int:todo_id>/',
        views.TodoDoneView.as_view(),
        name='todo-done'
    )
]
