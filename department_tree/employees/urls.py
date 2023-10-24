from django.urls import path
from .views import DepartmentTreeView

urlpatterns = [
    path('department-tree/', DepartmentTreeView.as_view(), name='department-tree'),
]
