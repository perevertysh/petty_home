from django.urls import path

from .views import IndexPageView, PetListView

urlpatterns = [
    path('pets/', PetListView.as_view()),
    path('', IndexPageView.as_view()),
]
