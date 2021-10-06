from django.apps import AppConfig

class ConcentrateursDemandeConfig(AppConfig):
    name = 'concentrateursDemande'

    def ready(self):
    	from Updater import updater
    	updater.start()