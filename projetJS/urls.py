"""projetJS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projetJS import settings
from django.conf.urls.static import static
from database.views import loginViews, disconnect
from dashboard.views import dashboard
from student.views import studentviews, deleteStudent, paymentViews
# from payment.views import paymentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginViews, name="login"),
    path('dash', dashboard, name="dashboard"),
    path('student/', studentviews, name="student"),
    path('student/delete/<int:id>', deleteStudent, name="delete-student"),
    path('payment/', paymentViews, name='payment'),
    path('disconnected/', disconnect, name="disconnect")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
