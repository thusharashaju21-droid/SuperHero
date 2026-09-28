from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hero.models import SuperHero
from hero_v2.serializer import HeroSerializer

# Create your views here.
class HeroCreateListView(APIView):

    def get(self,request):

        qs = SuperHero.objects.all()

        serial_instance = HeroSerializer(qs,many = True)

        return Response(data=serial_instance.data)


    def post(self,request):

        form_data = request.data

        serializer_instance = HeroSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            SuperHero.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)


        else:

            return Response(data=serializer_instance.error)


class HeroUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs=SuperHero.objects.get(id=pk)

        serializer_instance = HeroSerializer(qs)

        return Response(data=serializer_instance.data)