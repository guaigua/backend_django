from django.db import models

# Create your models here.
# From Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from apps.utils.models import RestorationsModel

from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.fields import GenericRelation

class Company(RestorationsModel):

    """
        Company model.

        Company model limit data to diferents company of company
    """
    name = models.CharField('name', max_length=30,unique=True)
    address = models.TextField(max_length=250)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    company = models.CharField('company name', max_length=30, blank=False)
    company_abbrevation = models.CharField('company abbreviation', max_length=5, blank=False)
    phone_contact = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    abbreviation = models.CharField('abbreviation', max_length=5, blank=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(
        'email address',
        max_length=30,
        unique=True,
        error_messages={
            'unique': 'A Company with that email already exists.'
        }
    )
    history = GenericRelation(LogEntry)

    def __str__(self):
        """Return name."""
        return self.name

    def get_short_name(self):
        """Return name."""
        return self.name