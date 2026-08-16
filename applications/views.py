from django.shortcuts import render, redirect, get_object_or_404

from .models import JobApplication


def home(request):

    applications = JobApplication.objects.all().order_by("-applied_date")

    total = applications.count()
    applied = applications.filter(status="Applied").count()
    interview = applications.filter(status="Interview").count()
    selected = applications.filter(status="Selected").count()
    rejected = applications.filter(status="Rejected").count()

    context = {
        "applications": applications,
        "total": total,
        "applied": applied,
        "interview": interview,
        "selected": selected,
        "rejected": rejected,
    }

    return render(
        request,
        "applications/home.html",
        context
    )


def add_application(request):

    if request.method == "POST":

        company_name = request.POST.get("company_name")
        job_role = request.POST.get("job_role")
        location = request.POST.get("location")
        applied_date = request.POST.get("applied_date")
        status = request.POST.get("status")
        notes = request.POST.get("notes")

        JobApplication.objects.create(
            company_name=company_name,
            job_role=job_role,
            location=location,
            applied_date=applied_date,
            status=status,
            notes=notes
        )

        return redirect("home")

    return render(
        request,
        "applications/add_application.html"
    )


def edit_application(request, id):

    application = get_object_or_404(
        JobApplication,
        id=id
    )

    if request.method == "POST":

        application.company_name = request.POST.get(
            "company_name"
        )

        application.job_role = request.POST.get(
            "job_role"
        )

        application.location = request.POST.get(
            "location"
        )

        application.applied_date = request.POST.get(
            "applied_date"
        )

        application.status = request.POST.get(
            "status"
        )

        application.notes = request.POST.get(
            "notes"
        )

        application.save()

        return redirect("home")

    return render(
        request,
        "applications/edit_application.html",
        {
            "application": application
        }
    )


def delete_application(request, id):

    application = get_object_or_404(
        JobApplication,
        id=id
    )

    if request.method == "POST":

        application.delete()

        return redirect("home")

    return render(
        request,
        "applications/delete_application.html",
        {
            "application": application
        }
    )


def application_detail(request, id):

    application = get_object_or_404(
        JobApplication,
        id=id
    )

    return render(
        request,
        "applications/application_detail.html",
        {
            "application": application
        }
    )