from api_site.sites import site
from api_site.models import ModelApi

from duct_tape.autodiscover import autodiscover as _ad
def autodiscover():
    _ad(module_name='api')

