import uuid

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from .validator import validate_msrp_format

from vendor.config import VENDOR_PRODUCT_MODEL

##################
# DEFAULTS
##################

# TODO: Nice to have class MSRP(NestedModels)

def product_meta_default():
    return {'msrp':{'default':'usd', 'usd':10.00}}

##################
# BASE MODELS
##################

class CreateUpdateModelBase(models.Model):
    '''
    This is a shared models base that provides created & updated timestamp fields
    '''
    created = models.DateTimeField("date created", auto_now_add=True)
    updated = models.DateTimeField("last updated", auto_now=True)

    class Meta:
        abstract = True


class ProductModelBase(CreateUpdateModelBase):
    '''
    This is the base class that all Products should inherit from.
    '''
    sku = models.CharField(_("SKU"), max_length=40, unique=True, blank=True, null=True, help_text=_("User Defineable SKU field"))   # Needs to be autogenerated by default, and unique from the PK
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)                                           # Used to track the product
    name = models.CharField(_("Name"), max_length=80, blank=False)
    site = models.ForeignKey(Site, verbose_name=_("Site"), on_delete=models.CASCADE, default=settings.SITE_ID, related_name="products")        # For multi-site support
    slug = AutoSlugField(populate_from='name', unique_with='site__id')                                                                         # Gets set in the save
    available = models.BooleanField(_("Available"), default=False, help_text=_("Is this currently available?"))        # This can be forced to be unavailable if there is no prices attached.
    description = models.JSONField(_("Description"), default=dict, blank=True, null=True)
    meta = models.JSONField(_("Meta"), default=product_meta_default, blank=True, null=True, help_text=_("Eg: { 'msrp':{'usd':10.99} }\n(iso4217 Country Code):(MSRP Price)"))
    classification = models.ManyToManyField("vendor.TaxClassifier", blank=True)                                        # What taxes can apply to this item
    offers = models.ManyToManyField("vendor.Offer", blank=True, related_name="products")
    reciepts = models.ManyToManyField("vendor.Receipt", blank=True, related_name="products")

    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_msrp(self, currency):
        if currency in self.meta['msrp']:
            return self.meta['msrp'][currency]
        else:
            return self.meta['msrp'][self.meta['msrp']['default']]
            
    def add_to_cart_url(self):
        """
        Link to add the item to the user's cart.
        """
    # TODO: ADD trigger when object becomes unavailable to disable offer if it exisits. 
