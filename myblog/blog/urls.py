from django.urls import path
from . import views


urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDitaidl.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
               path('<int:pk>/add_dislikes/', views.AddDisLike.as_view(), name='add_dislikes')]

