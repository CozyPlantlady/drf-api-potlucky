from django.urls import path
from comments import views
from recipes import views

urlpatterns = [
    path('recipes/<int:pk>/comments/', views.CommentList.as_view()),
    path('recipes/<int:pk>/comments/<int:pk>/', views.CommentDetail.as_view()),
]
