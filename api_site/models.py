from piston.resource import Resource
from piston.handler import BaseHandler

from django.conf.urls.defaults import patterns,url,include

class ModelApi(object):
    emitter_format = 'json'
    fields = ()
    handler = BaseHandler
    url_attrs = {}

    def __init__(self,model): 
        self.model = model

    def get_urls(self):
        # Create Handler
        # Give this new form class a reasonable name.
        handler_class_name = self.model.__name__ + 'Handler'

        # Class attributes for the new form class.
        handler_class_attrs = {
                'model':self.model
        }
        if self.fields:
            handler_class_attrs['fields']=self.fields

        handler_class = type(handler_class_name, (self.handler,), handler_class_attrs)
        resource = Resource(handler_class)

        url_attrs = self.url_attrs
        if self.emitter_format:
            url_attrs['emitter_format'] = self.emitter_format

        return patterns('',
            (r'^%s/'%'fi',
                include( 
                    patterns('',
                        url(r'^$', resource,  url_attrs, name='list'),
                        url(r'^(?P<id>\d+)/$', resource, url_attrs, name='show'),
                    ),namespace='fi',app_name='fi'
                )
            ),
        )
        return 



        #class BaseGenericExtAPIEngine(object):
        #    # you will have to extend the view classes and then override these
        #    handler_klass = BaseExtHandler
        #
        #    @classmethod
        #    def get_patterns(
        #            klass,
        #            model,
        #            app_path,
        #            alternate_url_prefix=None,
        #            fields=None,
        #            search_fields=None,
        #            **kwargs):
        #
        #        model_name = model.__name__.lower() 
        #        if not app_path=="":
        #            app_path += ':'
        #
        #        if not alternate_url_prefix:
        #            alternate_url_prefix = model_name
        #
        #        app_path += alternate_url_prefix
        #
        #
        #
        #        #TODO: figure out how you want to handle api/fis/fi
    @property
    def urls(self):
        return self.get_urls()

