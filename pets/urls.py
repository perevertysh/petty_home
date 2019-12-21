from django.urls import path

from .views import IndexPageView, PetListView, ContactsView

urlpatterns = [
    path('', IndexPageView.as_view()),
    path('pets/', PetListView.as_view()),
    path('contacts/', ContactsView.as_view())
]
