from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alx_backend_caching_property_listings.properties'

    def ready(self):
        import properties.signals
