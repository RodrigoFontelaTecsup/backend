from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()


def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    ##
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('choose another email')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not username:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('se necesita un correo electronico')
    return True


def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('elija otro nombre de usuario')
    return True


def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('se necesita una contraseña')
    return True
