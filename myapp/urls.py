from django.urls import path
from .views import*


urlpatterns = [
    #### generic url route #########
    path('generic-student/', StudentGeneric_view.as_view()),
    path('generic-student/<id>/', Student_Upadte_Delete.as_view()),

    path('student/' ,StudentAPI.as_view()),
    path('register/', UserRigistration.as_view()),
    path('register-token/', UserRigistration_Token.as_view())

    #path('student/' ,StudentAPI.as_view())

    ########## using decorator api_view ###########
    # path('', Get),
    # path('student-post/', Post),
    # path('student-update/<id>/', Update),
    # path('student-delete/<id>/', Delete),
   # path('student-book/', get_book)
    
]