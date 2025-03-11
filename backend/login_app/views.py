from django.shortcuts import render
from rest_framework.response import Response
from orders.models import Historias, Ordenes, Laboratorios, Laboratorio, Pruebas, Ordenesdet, Estudios, Estudiosdet, Centros_eps, Servicios, Tecnicasprueba, Appusers, LaboratoriosRem
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['POST'])
def get_login(request):
    usr_identification = request.data.get('userLogin')
    usr_em_nit = request.data.get('labNit')
    password = request.data.get('password') 
    print("request", usr_identification, password, usr_em_nit)

    try:
        user = Appusers.objects.get(usr_identification=usr_identification, usr_em_nit=usr_em_nit)
        print("user", user)
        if user.is_active:
            if check_password(password, user.usr_password):
                refresh = RefreshToken.for_user(user)
                
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'usr_id': user.usr_id,
                    'usr_name': user.usr_name
                })
            else:
                return Response({'error': 'Credenciales inválidas'}, 
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Usuario inactivo'}, 
                        status=status.HTTP_401_UNAUTHORIZED)
        
    except Appusers.DoesNotExist:
        return Response({'error': 'Usuario no encontradoO'}, 
                       status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET', 'POST'])
@authentication_classes([CustomJWTAuthentication])
@permission_classes([IsAuthenticated])
def get_User(request):
    #print("request:", request)
     # Inspeccionar los datos de la solicitud
    user = request.user
    return Response({
        'username': user.usr_name,
        'email': user.usr_email,
        'id': user.usr_id,
        'load_resRem': user.load_resRem
    }) 
