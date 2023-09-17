from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.Entry, name="entry"),
    path("search/", views.Search, name="search"),
    path("new_entry_page/", views.NewEntryPage, name="new_entry_page"),
    path('edit_entry/', views.EditEntry, name='edit_entry'),
    path('save_entry/', views.EditSave, name='save_entry'),
    path('random_page/', views.RandomPage, name='random_page')
    
]
