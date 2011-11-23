from piston.resource import Resource
from piston.handler import BaseHandler

from django.conf.urls.defaults import patterns,url,include

class ModelApi(object):
    emitter_format = 'json'
    fields = ()
    search_fields = ()
    handler = BaseHandler
    url_attrs = {}

    def __init__(self,model,**kwargs): 
        self.model = model
        for k,v in kwargs.items():
            self.__dict__[k] = v

    def get_urls(self):
        if not hasattr(self,'name'): self.name = self.model.__name__
        # Create Handler
        # Give this new form class a reasonable name.
        handler_class_name = self.name + 'Handler'

        # Class attributes for the new form class.
        handler_class_attrs = {
                'model':self.model
        }
        if self.fields:
            handler_class_attrs['fields']=self.fields

        if self.search_fields:
            handler_class_attrs['search_fields']=self.search_fields

        handler_class = type(handler_class_name, (self.handler,), handler_class_attrs)
        resource = Resource(handler_class)

        url_attrs = self.url_attrs
        if self.emitter_format:
            url_attrs['emitter_format'] = self.emitter_format

        name = self.name.lower()

        return patterns('',
            (r'^%s/'%name,
                include( 
                    patterns('',
                        url(r'^$', resource,  url_attrs, name='list'),
                        url(r'^(?P<id>\d+)/$', resource, url_attrs, name='show'),
                    ),namespace=name,app_name=name
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

