from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Class

from .forms import ClassForm

from django.shortcuts import render, redirect


class ClassCreateView(CreateView):
    template_name = 'class/create_class.html'  # scriem calea catre pagina html unde vom gasi formularul generat
    model = Class
    # fields = '__all__' # preia toate fielduril din model si in interfata va fi in ordinea declarata in models.py
    form_class = ClassForm
    success_url = reverse_lazy('class_index')


def index(request):
    class_list = Class.objects.order_by("-date")
    context = {
        "class_list": class_list,
    }
    return render(request, "class/index.html", context)


def class_details(request, id):
    class_obj = get_object_or_404(Class, pk=id)
    context = {"class_var": class_obj}
    return render(request, "class/details.html", context)


def class_remove(request, id):
    class_obj = get_object_or_404(Class, pk=id)
    class_obj.delete()
    return redirect("/class/")
