from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'pfsite/index.html'

class ProjectView(TemplateView):
    template_name = 'pfsite/projects.html'

class ResumeView(TemplateView):
    template_name = 'pfsite/resume.html'
