from .models import  CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout



@api_view(['GET'])
def getData(request):
    output = [{"id": user.id, "username": user.username, "email": user.email}
              for user in CustomUser.objects.all()]
    return Response(output)



@api_view(['GET'])
def get_user_by_id(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "isSupervisor":user.isSupervisor
        }
        return Response(user_data)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    

@api_view(['POST'])
def SignUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    print(request.data)
    if 'email' in request.data and 'password' in request.data:
        email = request.data.get('email')
        password = request.data['password']

        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"message": "Login successful!", "access_token": access_token})
        else:
            return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({"message": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Logout(request):
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful!"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": "Error logging out"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.contrib.auth import get_user
from django.http import JsonResponse
@api_view(['GET'])
def is_admin_connected(request):
    user = get_user(request)
    if user.is_authenticated and (user.is_staff or user.is_superuser):
        return JsonResponse({"status": "Admin is connected"})
    else:
        return JsonResponse({"status": "No admin is connected"})        
   