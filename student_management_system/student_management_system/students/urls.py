from django .urls import path
from .import views

urlpatterns=[
    path('display_student/',views.display_student_view,name='display'),
    path('create-student/',views.create_student_view,name='create'),
    path('update-student/<int:student_id>/',views.update_student_view,name='update'),
    path('delete-student/<int:student_id>/',views.delete_student_view,name='delete')
]