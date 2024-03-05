from django.urls import path
from . import views
urlpatterns =[
     path('home/', views.Homepage, name='home-page'),
     path('register/', views.register, name='register-page'),
     path('login/', views.Login, name='login-page'),
     path('logout/', views.logoutuser, name='logout'),
     path('make_payment/', views.make_payment , name='make_payment' ),
     path('book_vehicle/', views.book_vehicle , name='book_vehicle'),
     path('vehicles/', views.vehicles, name='vehicles'),
     path('landing_page/', views.landing_page, name='landing_page'),
     path('update_database/', views.update_database, name='update_database'),
     path('return_vehicle/', views.return_vehicle, name='return_vehicle'),

]