
from django.urls import path
from directory.api.views.login_views import CustomAuthToken
from directory.api.views.user_views import UsersViewSet


urlpatterns = [
    path('auth/', CustomAuthToken.as_view()),
    path('user/company/<str:company_id>', UsersViewSet.get_Users, name= "user" ),
    path('user/reports_to/<str:reports_to_id>', UsersViewSet.get_Hierarchy, name= "reports" ),
    path('user/reports_to_inv/<int:user_id>', UsersViewSet.get_Hierarchy_inv, name= "reports_inv")
]
