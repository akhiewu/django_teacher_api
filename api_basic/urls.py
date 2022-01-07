
from django.urls import path
from .views import teacher_list, teacher_detail
#TeacherAPIView,TeacherDetails

urlpatterns = [
    
    path('teacher/', teacher_list),
    path('detail/<int:pk>/', teacher_detail),
    #path('teacher/', TeacherAPIView.as_view()),
    #path('detail/<int:id>/', TeacherDetails.as_view())
    
]