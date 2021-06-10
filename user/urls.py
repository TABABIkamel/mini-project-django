from django.urls import path

from user import views
#from user.views import formation_ListView

urlpatterns=[
    #path('ListView/',formation_ListView.as_view(),name='lf'),
    path('ListView/',views.Get_List,name='lf'),
    path('Login/', views.login_user, name='login'),
    path('Signup/', views.signup, name='signup'),
    path('logout/',views.logout_user,name='logout'),

]