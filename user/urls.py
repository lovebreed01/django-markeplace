from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views



urlpatterns = [
	path('user/profile/',views.profile, name='profile'),
	path('user/login/', views.login_view , name='login' ),
	path('user/logout/', LogoutView.as_view(template_name='landing/logout.html'), name='logout' ),
	path('user/signup/', views.signup, name='signup' ),
	path('user/complete/',views.complete_reg,name='complete-reg')
]

