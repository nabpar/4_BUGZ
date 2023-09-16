from django.urls import path
from . import views


urlpatterns = [
    path("user/registration/",views.UserRegistrationView.as_view(),name="user registration path"),
    path('user/login/',views.UserLoginView.as_view(),name="user login path"),
    # path("login/user/profile/", views.UserLogin_profile.as_view(), name="login user path"),


    ######

    path('act_view/',views.ActionUser_ListView.as_view(),name="act_view"),
    path('act_create/',views.ActionUser_Create.as_view(),name="act_create"),
    path('act_update/',views.ActionUser_Update.as_view(),name="act_update"),
    path('act_destroy/',views.ActionUser_Destroy.as_view(),name="act_destroy"),


## url path for Resource uploader
    path('res_view/',views.Resource_Veiw.as_view(),name="res_view"),
    path('res_create/',views.Resource_Create.as_view(),name="res_create"),
    path('res_upload/',views.Resource_Update.as_view(),name="res_upload"),
    path('res_destroy/',views.Resource_Destroy.as_view(),name="res_destroy"),

    path('login/user/profile/<int:pk>/',views.UserLoginView.as_view(),name="login user profile path"),
    path('act_search/',views.ActionUser_ListView.as_view(),name="path to search the product"),
    
        
]
