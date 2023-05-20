from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from member.models import Member

from member.forms import MemberForm


class MemberCreateView(CreateView):
    template_name = 'member/create_member.html'  # scriem calea catre pagina html unde vom gasi formularul generat
    model = Member
    # fields = '__all__' # preia toate fielduril din model si in interfata va fi in ordinea declarata in models.py
    form_class = MemberForm
    success_url = reverse_lazy('member_index')


def index(request):
    members_list = Member.objects.order_by("-expiry_date")
    context = {
        "members_list": members_list,
    }
    return render(request, "member/index.html", context)


def member_details(request, cnp):
    member = get_object_or_404(Member, pk=cnp)
    context = {"member": member}
    return render(request, "member/details.html", context)


def member_remove(request, cnp):
    member = get_object_or_404(Member, pk=cnp)
    member.delete()
    return redirect("/member/")
