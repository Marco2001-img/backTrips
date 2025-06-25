from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.customers.views import RegisterView, LoginView, ClienteViewSet

# 🔧 Aquí defines el router
router = DefaultRouter()
router.register(r'', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),  # ✅ Aquí ya se puede usar
]
