from django.urls import path
from .views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('clothes_and_shoes/', MainView.as_view(), name='clothes_and_shoes'),
    path('clothes_and_shoes/clothes/', MainView.as_view(), name='clothes'),
    path('clothes_and_shoes/shoes/', MainView.as_view(), name='shoes'),
    path('clothes_and_shoes/clothes/clothes_man/', MainView.as_view(), name='clothes_man'),
    path('clothes_and_shoes/clothes/clothes_woman/', MainView.as_view(), name='clothes_woman'),

    path('summer/', MainView.as_view(), name='summer'),
    path('winter/', MainView.as_view(), name='winter'),
    path('summer/rain/', MainView.as_view(), name='rain'),
    path('summer/sunny/', MainView.as_view(), name='sunny'),
]
