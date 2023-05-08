from django.shortcuts import render, get_object_or_404, redirect

from .models import Member


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
