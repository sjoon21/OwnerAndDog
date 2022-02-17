from django.urls import path

from owners.views import OwnersView, DogsView

urlpatterns = [
    path('/owner', OwnersView.as_view()),
    path('/dog', DogsView.as_view())
]