from django.urls import path
from memories import views

urlpatterns = [
    path('my-memories/', views.my_memories, name='my_memories'),
    path('new-memory/', views.new_memory, name='new_memory'),
]