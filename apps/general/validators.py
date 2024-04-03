from django.core.validators import ValidationError


def phone_validate(phone_number: str) -> None:
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('Phone number must be 13 numbers!!!')