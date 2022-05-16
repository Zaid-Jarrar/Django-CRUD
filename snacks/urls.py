from django.urls import path
from .views import (HomeView,
                    SnackCreateView,
                    SnackDetailView,
                    SnackUpdateView,
                    SnackDeleteView,
                    SnackListView,)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name='update_snack'),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name='delete_snack'),
    path('snack-list', SnackListView.as_view(), name='snack_list'),

]