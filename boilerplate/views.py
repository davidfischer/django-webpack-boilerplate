from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    http_method_names = ['get']
