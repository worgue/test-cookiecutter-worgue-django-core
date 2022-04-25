from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import logout_then_login
from .urlhelper import required

mypage_patterns = (required(
    login_required,
    [
        # path('', include('{{cookiecutter.project_slug}}.apps.accounts.mypageurls')),
    ]
), 'mypage')

urlpatterns = [
    # path('mypage/', include(mypage_patterns, namespace='mypage')),
    path('',
         TemplateView.as_view(template_name='userpage/home.html'), name='home'),
    path('accounts/logout/', logout_then_login, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# admin
urlpatterns += [
    path('admin/', admin.site.urls),
]

# media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
