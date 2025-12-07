
# annick_beauty_api/urls.py
# ... other imports (admin, path, include, TokenObtainPairView, etc.)
#
# Add this line temporarily to test the import:
# import ecom_api.urls 
# 
# After you test the import, comment it out or remove it.
# ...
# annick_beauty_api/urls.py
from django.contrib import admin
from django.urls import path, include # COMBINED path and include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT Authentication Endpoints
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # App Endpoints
    path('api/', include('ecom_api.urls')),
    
    # Note: The comment "# Leave this list empty for now..." should be moved 
    # to your ecom_api/urls.py file, not here in the main urls.py.
]