"""
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

"""
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from collector.forms.creature_form import CreatureForm
from collector.models.creatures import Creature


class CreatureDetailView(DetailView):
    model = Creature
    context_object_name = 'c'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatureUpdateView(UpdateView):
    model = Creature
    form_class = CreatureForm
    context_object_name = 'c'
    template_name_suffix = '_form'
