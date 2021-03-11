# from django.shortcuts import render
from core.saving.models import Saving
from django.views.generic import *


class SavingListView(ListView):
    model = Saving
    template_name = 'saving/saving.html'


class SavingCreateView(CreateView):
    pass


class SavingUpdateView(UpdateView):
    pass


class SavingDeleteView(DeleteView):
    pass
