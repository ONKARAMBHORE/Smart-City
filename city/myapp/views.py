from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Report
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count


# ---------------------------
# HOME PAGE
# ---------------------------
def index(request):
    qs = Report.objects.order_by('-created_at')

    # Filters
    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    status = request.GET.get('status', '').strip()

    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(description__icontains=q)
    if category:
        qs = qs.filter(category=category)
    if status:
        qs = qs.filter(status__iexact=status)

    recent_reports = qs[:12]

    # Stats
    total_reports = Report.objects.count()
    status_counts = Report.objects.values('status').annotate(count=Count('id')).order_by('-count')
    category_counts = Report.objects.values('category').annotate(count=Count('id')).order_by('-count')

    # Category options from model choices
    categories = [c[0] for c in Report.CATEGORY_CHOICES]

    context = {
        'recent_reports': recent_reports,
        'total_reports': total_reports,
        'status_counts': status_counts,
        'category_counts': category_counts,
        'categories': categories,
        'filter_q': q,
        'filter_category': category,
        'filter_status': status,
    }

    return render(request, "index.html", context)


# ---------------------------
# USER REGISTRATION
# ---------------------------
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Username exists?
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")

        # Email exists?
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect("register")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "register.html")


# ---------------------------
# USER LOGIN
# ---------------------------
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("add_report")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")


# ---------------------------
# USER LOGOUT
# ---------------------------
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("index")


# ---------------------------
# ADD REPORT
# ---------------------------
def add_report(request):
    if not request.user.is_authenticated:
        return redirect("login")  # Protect the page

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        location = request.POST.get("location")
        image = request.FILES.get("image")

        report = Report(
            user=request.user,
            title=title,
            description=description,
            category=category,
            location=location,
            image=image,
        )
        report.save()

        messages.success(request, "Issue reported successfully!")
        return redirect("add_report")

    return render(request, "add_report.html")


# ---------------------------
# STAFF DASHBOARD
# ---------------------------
@staff_member_required
def staff_dashboard(request):
    # Basic stats
    total_reports = Report.objects.count()
    status_counts = Report.objects.values('status').annotate(count=Count('id')).order_by('-count')
    category_counts = Report.objects.values('category').annotate(count=Count('id')).order_by('-count')

    # Recent reports
    recent_reports = Report.objects.order_by('-created_at')[:12]

    context = {
        'total_reports': total_reports,
        'status_counts': status_counts,
        'category_counts': category_counts,
        'recent_reports': recent_reports,
    }

    return render(request, 'admin_dashboard/dashboard.html', context)
