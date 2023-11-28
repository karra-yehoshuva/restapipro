from rest_framework import serializers
from .models import Student,Category,Book
from django.contrib.auth.models import User

############### user serializer #############
# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         feilds = ['username','password']
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user




class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name',]
        #fileds = '__all__'
#nested serializer

class BookSerializer(serializers.ModelSerializer):
    #category = CategorySerializer(source = 'category_id')
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
        #depth = 1

