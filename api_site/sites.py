from api_site.models import ModelApi

class ApiSite(object):
    def __init__(self, name=None, app_name='api'):
        self._registry = {} # model_class class -> admin_class instance
        if name is None:
            self.name = 'api'
        else:
            self.name = name
        self.app_name = app_name

    def register(self,model,config_class=None,**kwargs):
        name = model.__name__
        if 'name' in kwargs: name = kwargs['name']

        if not config_class: config_class = ModelApi
        self._registry[name] = config_class(model,**kwargs)

    def unregister(self,name):
        del(self._registry,name)

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url, include

        # todo:
        # django-duct-tape??
        #if settings.DEBUG:
        #    self.check_dependencies()

        #def wrap(view, cacheable=False):
        #    def wrapper(*args, **kwargs):
        #        return self.admin_view(view, cacheable)(*args, **kwargs)
        #    return update_wrapper(wrapper, view)

        # site-wide views.
        # use this for documentation generation?
        #urlpatterns = patterns('',
        #    url(r'^$',
        #        wrap(self.index),
        #        name='index'),
        #    url(r'^(?P<app_label>\w+)/$',
        #        wrap(self.app_index),
        #        name='app_list')
        #)
        urlpatterns = []

        # Add in each model's views.
        for model_name, model_api_config in self._registry.iteritems():
            app = model_api_config.model._meta.app_label
            urlpatterns += patterns('',
                url(r'^%s/' % app,
                    include(
                        model_api_config.urls, 
                        namespace=app, 
                        app_name=app))
            )
        return urlpatterns

    def autodiscover(self):
        from duct_tape.autodiscover import autodiscover as _ad
        _ad(module_name=self.app_name)

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.name

site = ApiSite()
