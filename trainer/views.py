from django.shortcuts import render, get_object_or_404, redirect

from trainer.models import Trainer


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

