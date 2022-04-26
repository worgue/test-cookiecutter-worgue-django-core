from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import logout_then_login
from .urlhelper import required

urlpatterns = [
    path('accounts/logout/', logout_then_login, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# admin
urlpatterns += [
    path('admin/', admin.site.urls),
]

# media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
