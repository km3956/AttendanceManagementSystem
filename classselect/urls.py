from django.urls import path
from .views import ClassSelectView

urlpatterns = [
    path('', ClassSelectView.as_view(), name='class-select'),
]