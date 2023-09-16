from django.shortcuts import render
from rest_framework.response import Response
from .serializer import UserRegistration_Serializer,UserLogin_Serializer,Userprofileserializer
from rest_framework.views import APIView
from rest_framework import generics ,status,permissions
from django.contrib.auth import authenticate
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializer import ActionUserDetail_Serializer



# # generating the token for the user.
# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#     }





# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistration_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # extracting the id of the registred user.
            uid = user.id
            # token = get_tokens_for_user(user)  # for the token...
            return Response(
                {
                    # "token": token,
                    "msg": "Registration Successful",
                    "uid": uid,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# user login view.
class UserLoginView(APIView):

    def post(self, request, format=None):
        serializer = UserLogin_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            uid=user.id
            # user_type = user.is_admin
            if user is not None:
                # token = get_tokens_for_user(user)
                return Response(
                    {
                        # "token":token,
                        "uid":uid,
                        "msg": "Login Successfully",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"msg": "Email or Password is not valide"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .serializer import ActionUser_Serialization,Resource_Serialization
from .models import ActionUser,ResourceUploader
# Create your views here.





## view class for ActionUser model

class ActionUser_ListView(generics.ListAPIView):
    queryset = ActionUser.objects.all()
    serializer_class = ActionUser_Serialization

class ActionUser_ListView(generics.ListAPIView):
    queryset = ActionUser.objects.all()
    serializer_class = ActionUser_Serialization
    filter_backends = [SearchFilter]
    search_fields = ["name"]

class ActionUser_Create (generics.CreateAPIView):
    queryset = ActionUser.objects.all()
    serializer_class = ActionUser_Serialization

class ActionUser_Update(generics.UpdateAPIView):
    queryset = ActionUser.objects.all()
    serializer_class = ActionUser_Serialization


class ActionUser_Destroy(generics.DestroyAPIView):
    queryset = ActionUser.objects.all()
    serializer_class = ActionUser_Serialization


## view class for ResourceUploader model 

class Resource_Veiw(generics.ListAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_Serialization

class Resource_Create(generics.ListAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_Serialization

class Resource_Update(generics.ListAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_Serialization

class Resource_Destroy(generics.ListAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_Serialization


# class UserLogin_profile(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         serializer = Userprofileserializer(request.user)

#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK,
#         )





class UserLoginView(APIView):
    def get (self,request, pk,format=None, *args, **kwargs):
        try:
            user_data=User.objects.get(id=pk)
            user_data_ac=ActionUser.objects.get(user=pk)
            print(user_data_ac)
            serializer = ActionUserDetail_Serializer(user_data_ac)
            return Response(serializer.data)

        except User.DoesNotExist:
            return Response(
                    {"msg": "The artist is not available in the database."},
                    status=status.HTTP_404_NOT_FOUND,
                )