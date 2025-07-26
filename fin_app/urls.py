from django.urls import path
from . import views
from . import chat

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_page, name='home_page'),
    path('home/getinfo/', views.get_investments, name='get_investments'),
    path('home/getinfo/compare/', views.compute_plans, name='compute_plans'),
    path('ajax/call_function/', chat.my_ajax_function, name='ajax_call_function'),
] 