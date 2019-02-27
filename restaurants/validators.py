from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

# def clean_email(self):
#     email = value
#     if '.edu' in email:
#         raise ValidationError("We don't not accept edu emails")

CATEGORIES = ['mexican', 'greek', 'american', 'italian', 'chinese', 'asian', 'korean', 'greek american fusion', 'middle eastern',]

def validate_category(value):
    cat = value.lower()
    if not value in CATEGORIES and not cat in  CATEGORIES:
        raise ValidationError(f'{value} is not valid category')