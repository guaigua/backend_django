# From Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from utils.models import RestorationsModel


class Clients(RestorationsModel):

    first_name = models.CharField('names', max_length=100)
    last_name = models.CharField('names', max_length=100)

    # # Username Field
    # username = serializers.CharField(
    #     min_length=4, 
    #     max_length=30,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A client with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # Address Fields
    address = models.TextField(max_length=250, null=True, blank=True) # -- Si requered
    city = models.CharField('city', max_length=30, null=True, blank=False) # -- Si requered
    state = models.CharField('state', max_length=30, null=True, blank=False)# -- Si requered
    zip_code = models.CharField('zip', max_length=30, null=True, blank=False)# -- Si requered
    country = models.CharField('country', max_length=30, null=True, blank=False)# -- Si requered
    
    county = models.CharField('county', max_length=30, null=True, blank=True)   # -- Si requered
    route = models.CharField('route', max_length=30, null=True, blank=True) # -- Si requered
    street_number = models.CharField('street number', max_length=30, null=True, blank=True) # -- Si requered
    neighborhood = models.CharField('neighborhood', max_length=30, null=True, blank=True) # -- Si requered
    latitude = models.DecimalField('latitude', max_digits=30, decimal_places=20, null=True, blank=True) # -- Si requered
    longitude = models.DecimalField('longitude', max_digits=30, decimal_places=20, null=True, blank=True) # -- Si requered

    def __str__(self):
        """Return username."""
        return self.first_name

    def get_short_name(self):
        """Return username."""
        return self.first_name