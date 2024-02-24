
from django.contrib import admin
from django.urls import path
from Mysqlcrud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"), # Localhost:8000
    path('insert/',views.insert),
    path('update/<int:id>',views.update),
    path('delete/<int:id>', views.delete),

]
