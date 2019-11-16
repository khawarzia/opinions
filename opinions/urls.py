from django.contrib import admin
from django.urls import path
from login import views as vlog
from posting import views as vpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vpost.base , name = 'base'),
    path('login', vlog.login , name = 'login'),
    path('signup', vlog.signup , name = 'signup'),
    path('logout', vlog.logout , name = 'logout'),
    path('profile', vpost.profile , name = 'profile'),
    path('new-post/<str:sel>', vpost.newpost , name = 'new-post'),
    path('counter-post/<int:id>/<str:sel>', vpost.counterpost , name = 'counter-post'),
    path('view-post/<int:id>', vpost.viewpost , name = 'view-post'),
    path('agree/<int:id>/<str:t>', vpost.agree , name = 'agree'),
    path('disagree/<int:id>/<str:t>', vpost.disagree , name = 'disagree'),
]