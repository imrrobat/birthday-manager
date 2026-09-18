from django.urls import path
from . import views

urlpatterns = [
    path("", views.BirthdayListView.as_view(), name="home"),
    path("add/", views.add_birthday, name="add"),
    path("delete/<int:id>/", views.delete_birthday, name="delete"),
    path('edit/<int:id>/', views.edit_birthday, name='edit_birthday'),
]