from django.shortcuts import render
from django.views import View
from .models import Department

class DepartmentTreeView(View):
    def get(self, request):
        top_departments = Department.objects.filter(parent__isnull=True)
        context = {'top_departments': top_departments}
        return render(request, 'department_tree.html', context)
