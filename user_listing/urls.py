from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_user_list', login_required(views.all_user_list_screen), name='all_user_list_screen'),
    path('all_user_list_api', login_required(views.all_user_list_api), name='all_user_list_api'),
    path('fetch_random_data_api', login_required(views.fetch_random_data_api), name='fetch_random_data_api'),
    path('fetch_random_data_screen', login_required(views.fetch_random_data_screen), name='fetch_random_data_screen'),
    path('clear_database_api', login_required(views.clear_database_api), name='clear_database_api'),
    path('search_users_screen', login_required(views.search_users_screen), name='search_users_screen'),
    path('get_filtered_data_api', login_required(views.get_filtered_data_api), name='get_filtered_data_api'),
    path('single_user_info/<str:userid>/', login_required(views.single_user_info), name='single_user_info'),
    path('fetch_large_random_data_for_load_test', login_required(views.fetch_large_random_data_for_load_test), name='fetch_large_random_data_for_load_test'),
    path('api_screen', views.api_screen, name='api_screen'),
    path('performance_screen', views.performance_screen, name='performance_screen'),
    
]