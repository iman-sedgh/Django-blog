from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [
    path('',PostListView,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('test/',views.test,name='blog-test'),
    

]
