from customers.views import TenantView, TenantViewRandomForm, TenantViewFileUploadCreate, TenantViewActionLog
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TenantView.as_view(), name="index"),
    path('sample-random/', TenantViewRandomForm.as_view(), name="random_form"),
    path('upload-file/', TenantViewFileUploadCreate.as_view(), name="upload_file"),
    path('action-log', TenantViewActionLog.as_view(), name='action_log'),
    path('test/', TemplateView.as_view(template_name='test.html'), name="test"),
    path('admin/', admin.site.urls),
    ]
