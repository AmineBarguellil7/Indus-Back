from  .models import  CustomUser
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import CustomUser



class UserView(APIView):
    def get(self,request):
        output=[{"id":output.id,"username":output.username,"email":output.email,"password":output.password}
        for output in CustomUser.objects.all()
        ]  
        return Response(output)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)      
