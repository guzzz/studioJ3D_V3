
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Project
from .serializers import ProjectCustomSerializer
from .choices import SPACE_CHOICES


class ProjectsPageView(TemplateView):
    template_name = 'projectsPage.html'

    def get(self, request, *args, **kwargs):
        space = request.GET.get("space")
        if space:
            img_list = Project.objects.filter(space=space).order_by('-position')
        else:
            img_list = Project.objects.filter(space='living room').order_by('-position')
            space = 'living room'

        json_list = []
        for item in img_list:
            json_list.append(ProjectCustomSerializer(item).data)

        return render(request, self.template_name, {'img_list':img_list, 'javascript_list':json_list, 'selected_filter':space})


class TPageView(TemplateView):
    template_name = '360Page.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        context = {
            'image': project.photo.url,
            'description' : project.description
        }
        return render(request, self.template_name, context)
