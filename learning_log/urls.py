from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
]

handler404 = 'learning_logs.views.custom_page_not_found_view'
handler500 = 'learning_logs.views.custom_error_view'
