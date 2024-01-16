# accounts/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from core.models import CustomUser, EmailConfirmation
from core.serializers import CustomUserSerializer


@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        confirmation = EmailConfirmation.objects.create(user=user)
        confirmation.save()

        send_activation_email(user.email, confirmation.token)

        return Response({'message': 'Регистрация прошла успешно. Проверьте Ваш email для активации.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_activation_email(email, token):
    subject = 'Активируйте Ваш аккаунт'
    message = f'Для активации аккаунта, кликните на ссылку: http://yourdomain.com/activate/{token}/'
    from_email = 'ЗДЕСЬ НАШ ЕМАЙЛ вставить'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


@api_view(['GET'])
def account_activation_sent(request):
    return Response({'message': 'На Ваш email address выслано письмо. Пройдите по ссылке для активации аккаунта.'})


@api_view(['GET'])
def activate(request, token):
    confirmation = get_object_or_404(EmailConfirmation, token=token)
    user = confirmation.user

    if user.is_active:
        return Response({'message': 'Аккаунт активирован.'}, status=status.HTTP_400_BAD_REQUEST)

    user.is_active = True
    user.save()
    return Response({'message': 'Аккаунт успешно активирован. Теперь можете зайти на сайт под Вашим аккаунтом.'})


@api_view(['GET'])
def employee_dashboard(request):
    # Проверка на принадлежность к группе работников (ваша логика)
    if request.user.is_authenticated and request.user.is_employee:
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
    else:
        return Response({'message': 'Доступ запрещен.'}, status=status.HTTP_403_FORBIDDEN)
