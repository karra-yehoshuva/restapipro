from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student,Book,Category
from .serializers import studentSerializer,BookSerializer,CategorySerializer,Userserializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

######################## Generic views #####################
from rest_framework import generics

class StudentGeneric_view(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

class Student_Upadte_Delete(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer
    lookup_field = 'id'



#################3for generating username and password ###############
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserRigistration(APIView):
    

    def post(self, request):
        serializer = Userserializer(data = request.data)
        if not serializer.is_valid():
            return Response({"status":403,"error": serializer.errors})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj = Token.objects.get_or_create(user=user)
        return Response({"status":200,"payload":serializer.data,"token":str(token_obj),"message":"created successfulyy!!!"})
        #return Response({"status":200,"payload":serializer.data,"token":str(token_obj),"message":"user created successfully"})

############################# generate username and password alog with token manually ########
from rest_framework_simplejwt.tokens import RefreshToken
class UserRigistration_Token(APIView):
    def post(self, request):
        serializer = Userserializer(data = request.data)
        if not serializer.is_valid():
            return Response({"status":403,"error": serializer.errors})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({"status":200,"payload":serializer.data,"refresh":str(refresh),
                         'access':str(refresh.access_token),"message":"created successfulyy!!!"})
        

################# using APIView ########################
class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication] #JWT authentication
    #authentication_classes = [TokenAuthentication] #session authentication
    permission_classes = [IsAuthenticated]
    def get(self, request):
        get_obj = Student.objects.all()
        serializer = studentSerializer(get_obj, many=True)
        return Response({'status':200, 'payload':serializer.data,'message':'data fetched'})
    

    def post(self, request):
        serializer = studentSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors ,'message':'some thing went wrong'})
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message': 'new record inserted'})
        #put_obj = Student.objects.get(id = request.get['id'])
    def put(self, request):
        put_obj = Student.objects.get(id = request.data['id'])
        serializer = studentSerializer(put_obj, data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'message':'something went wrong'})
        
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'record updated successfully!!'})
    
    def patch(self, request):
        put_obj = Student.objects.get(id = request.data['id'],)
        serializer = studentSerializer(put_obj, data=request.data , partial = True)
        if not serializer.is_valid():
            return Response({'status':403, 'message':'something went wrong'})
        
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'record updated successfully!!'})


    def delete(self, request):
        try:
            del_obj = Student.objects.get(id=request.data['id']).delete()
            #del_obj = Student.objects.filter(id = request.data['id']).delete()
            print(del_obj)
            return Response({'status':200,'message':'deleted'})
        

        except Exception as e :
            print(e)

            return Response({'status':404, 'message':'invalid id'})

        

#     data = request.data
#     serializer = studentSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({'status':403,'errors':serializer.errors,'error':'something went wrong'})
#     serializer.save()      
#     return Response({'status':'ok','payload':serializer.data,'message':'you-sent'})


# Create your views here.
############################# using decorator api_view###############
# @api_view(['GET'])
# def Get(request):
#     query_set = Student.objects.all()
#     myserializer = studentSerializer(query_set, many = True)
#     return Response({'status':200,'payload':myserializer.data})


# @api_view(['POST'])
# def Post(request):
#     data = request.data
#     serializer = studentSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({'status':403,'errors':serializer.errors,'error':'something went wrong'})
#     serializer.save()      
#     return Response({'status':'ok','payload':serializer.data,'message':'you-sent'})

# @api_view(['PUT'])
# def Update(request,id):
#     try:

#         student_obj = Student.objects.get(id = id)
#         serializer = studentSerializer(student_obj,data = request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
#         serializer.save()
#         return Response({'status':200,'payload':serializer.data,'message':'data saved'})
#     except Exception as e:
#         print(e)

#         return Response({'status':403,'message':'invalid'})
    
# @api_view(['DELETE'])
# def Delete(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200,'message':'deleted'})

#     except Exception as e:
#         print(e)

#         return Response({'status':403,'message':'invalid id'})
    
# # Nested Serializer    
# @api_view(['GET'])
# def get_book(request):
#     book_obj = Book.objects.all()
#     serializer = BookSerializer(book_obj,many = True)
#     return Response({'status':200, 'payload':serializer.data ,'message':'Datafetched'})




    
