from django.urls import path
from .views import (
    PersonListCreateView,
    PersonRetrieveUpdateDestroyView,
    create_person,
    get_person,
    update_person,
    delete_person,
)

urlpatterns = [
    path('', PersonListCreateView.as_view(), name='person-list-create'),
    path('<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),
    #path('create_person/', create_person, name='create-person'),
    path('<int:pk>/', get_person, name='get-person'),
    path('<int:pk>/', update_person, name='update-person'),
    path('<int:pk>/', delete_person, name='delete-person'),
]
