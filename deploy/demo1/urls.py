from django.urls import path
from demo1.views import DeployView

urlpatterns = [
    path('student/',DeployView.as_view(),name='DeployApi')
]
