from django.shortcuts import render, get_object_or_404, redirect

from trainer.models import Trainer

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TrainerForm

class TrainerCreateView(CreateView):
    template_name = 'trainer/create_trainer.html'  # scriem calea catre pagina html unde vom gasi formularul generat
    model = Trainer
    # fields = '__all__' # preia toate fielduril din model si in interfata va fi in ordinea declarata in models.py
    form_class = TrainerForm
    success_url = reverse_lazy('trainer_index')


def index(request):
    trainers_list = Trainer.objects.order_by("-date_of_birth")
    context = {
        "trainers_list": trainers_list,
    }
    return render(request, "trainer/index.html", context)


def trainer_details(request, cnp):
    trainer = get_object_or_404(Trainer, pk=cnp)
    context = {"trainer": trainer}
    return render(request, "trainer/details.html", context)


def trainer_remove(request, cnp):
    trainer = get_object_or_404(Trainer, pk=cnp)
    trainer.delete()
    return redirect("/trainer/")

