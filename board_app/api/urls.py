
from django.urls import include, path
from rest_framework import routers
from .views import BoardListCreateView, BoardRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView

router = routers.SimpleRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('boards/', BoardListCreateView.as_view(), name='board-list-create'),
    path('boards/<int:pk>/', BoardRetrieveUpdateDestroyView.as_view(), name='board-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]