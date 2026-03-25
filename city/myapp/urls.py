from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("add-report/", views.add_report, name="add_report"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
]
