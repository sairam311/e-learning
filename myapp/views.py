from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from .serializers import *
import string,random

def generate_unique_user_code(length=8):
    characters = string.ascii_letters + string.digits  # a-z + A-Z + 0-9
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not students.objects.filter(user_code=code).exists():
            return code

class CreateUserView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['password'] = make_password(data.get('password'))
        data['user_code'] = generate_unique_user_code()

        referal_input = data.get('referal_code', '').strip()

        if referal_input:
            try:
                referrer = students.objects.get(user_code=referal_input)
                data['referal_code']=referal_input
                data['referal_email'] = referrer.email  # Store email of referrer
            except students.DoesNotExist:
                return Response({"referal_code": "Invalid referral code. Please check and try again."},status=status.HTTP_400_BAD_REQUEST)
        else:
            data['referal_code'] = ''  # Leave blank if not provided

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = students.objects.get(email=email)
        except students.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, user.password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = students.objects.get(email=email)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except students.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
