from. import views
from django.urls import path
app_name='filmapp'
urlpatterns = [


    path('',views.movies,name='movie'),
    path('theatre/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.updation,name='updation'),
    path('delete/<int:id>/',views.deletion,name='deletion')
]
