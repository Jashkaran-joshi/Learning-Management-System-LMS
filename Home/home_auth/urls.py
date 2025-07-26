from django.urls import path
from . views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password_view, name='reset-password'),
    path('logout/', logout_view, name='logout'),
    path('blank/', blank_page, name='blank_page'),
    path('profile/', view_profile, name='view_profile'),
    path('inbox/', view_inbox, name='view_inbox'),
]