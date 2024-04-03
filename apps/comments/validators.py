from django.core.validators import ValidationError


def rating_validate(rate):
    if not (1<= rate <= 5):
        raise ValidationError('rate must be enter between [1, 5]')