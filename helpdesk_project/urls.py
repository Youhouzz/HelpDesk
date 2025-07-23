from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def root_view(request):
    return JsonResponse({
        "message": "Bienvenue dans l'API Helpdesk 🎫",
        "endpoints": {
            "tickets": "/api/tickets/",
            "auth": "/api/users/auth/",
            "signup": "/api/users/auth/users/",
        }
    })

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),

    #  Djoser
    path('api/users/auth/', include('djoser.urls')),                # /users/, /users/me/
    path('api/users/auth/', include('djoser.urls.authtoken')),     # /token/login, /token/logout

    #  Users
    path('api/users/', include('users.urls')),
]
