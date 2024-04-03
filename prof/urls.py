from django.urls import path,re_path
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include,re_path

admin_router = DefaultRouter()
# router.register(r'api/admin', AdminsApi)
admin_router.register(r'api/users', AdminUserViewSet, basename='admin')
admin_router.register(r'api/universities', UniversitiesApi, basename='universities')
admin_router.register(r'api/proffessions', ProffessionsApi, basename='proffessions')
admin_router.register(r'api/internships', InternshipsApi, basename='internships')
admin_router.register(r'api/news', NewsApi, basename='news')


urlpatterns = [
    path('', include(admin_router.urls)),
    path('login/', CustomTokenCreateView.as_view(), name='admin_token_create'),
    path('register/', AdminUserCreateView.as_view(), name='admin_create'),
    path('send_reset_code/', send_reset_code, name='send_reset_code'),
    path('verify_reset_code/', verify_reset_code, name='verify_reset_code'),
    path('reset_password/', reset_password, name='reset_password'),
    path('verify_email/', send_verification_code, name='send_verification_code'),
    path('confirm_email/',confirm_verification_code,name='confirm_verification_code'),
    # path('api/universities/', UniversitiesApi.as_view(), name='universities'),
    # path('api/proffessions/', ProffessionsApi.as_view(), name='proffessions'),
    # path('api/internships/', InternshipsApi.as_view(), name='internships'),
    # path('api/news/', NewsApi.as_view(), name='news'),
    path('api/available_university/', UniversitiesApi.as_view({'get': 'available_university'}), name='available_university'),
    path('users/me/', UserMeView.as_view(), name='user-me'),
]