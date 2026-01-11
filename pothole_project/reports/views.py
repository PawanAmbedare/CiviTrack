from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from .models import PotholeReport
from .forms import PotholeReportForm

def home(request):
    return render(request, 'home.html')

def report_pothole(request):
    if request.method == 'POST':
        form = PotholeReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report submitted successfully. Thank you!')
            return redirect(reverse('dashboard'))
    else:
        form = PotholeReportForm()

    return render(request, 'report_pothole.html', {'form': form})

def dashboard(request):
    reports = PotholeReport.objects.order_by('-created_at')
    severity = request.GET.get('severity')
    status = request.GET.get('status')
    if severity in dict(PotholeReport.SEVERITY_CHOICES):
        reports = reports.filter(severity=severity)
    if status in dict(PotholeReport.STATUS_CHOICES):
        reports = reports.filter(status=status)

    context = {
        'reports': reports,
        'severity_choices': PotholeReport.SEVERITY_CHOICES,
        'status_choices': PotholeReport.STATUS_CHOICES,
        'selected_severity': severity or '',
        'selected_status': status or '',
    }
    return render(request, 'dashboard.html', context)


@require_POST
@user_passes_test(lambda u: u.is_staff)
def update_status(request, pk):
    report = get_object_or_404(PotholeReport, pk=pk)
    new_status = request.POST.get('status')
    valid_keys = [k for k, _ in PotholeReport.STATUS_CHOICES]
    if new_status in valid_keys:
        report.status = new_status
        report.save()
        messages.success(request, 'Status updated.')
    else:
        messages.error(request, 'Invalid status selected.')
    return redirect(reverse('dashboard'))
