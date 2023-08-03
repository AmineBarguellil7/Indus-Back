from .models import  CustomUser
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET'])
def getData(request):
    output = [{"id": user.id, "username": user.username, "email": user.email}
              for user in CustomUser.objects.all()]
    return Response(output)

@api_view(['POST'])
def SignUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def login(request):
#     # Check if 'email' and 'password' are present in the request data
#     if 'email' in request.data and 'password' in request.data:
#         email = request.data['email']
#         password = request.data['password']

#         # Authenticate user
#         user = authenticate(email=email, password=password)

#         if user:
#             # If user is authenticated, you can generate a token or session here
#             # and return it in the response. For simplicity, let's just return a success message.
#             return Response({"message": "Login successful!"})
#         else:
#             return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
#     else:
#         # If 'email' or 'password' is missing, it means it's a registration request
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    