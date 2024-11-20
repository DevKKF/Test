import datetime
# import the logging library
import logging

from django.http import JsonResponse
from comptabilite.views import alert_consumption, create_periode_comptable
from django_dump_die.middleware import dd

from configurations.helper_config import send_notification_background_task_mail
from configurations.models import CronLog
from shared import veos
from shared.veos import import_sinistre_manuellement_cron
from sinistre.helper_sinistre import load_backgroound_request_task

from sinistre.models import Sinistre

# Get an instance of a logger
logger = logging.getLogger(__name__)


def cron_all_once(request):
    dd("EXECUTION DES TACHES CRONS A LA SUITE ")



def cron_pays(request):
    data = veos.get_pays_lists()

    CronLog.objects.create(action="import", table="pays", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)


def cron_bureau(request):
    data = veos.get_bureaux_lists() # A revoir

    CronLog.objects.create(action="import", table="bureau", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)

def cron_devise(request):
    data = veos.get_devise_lists()

    CronLog.objects.create(action="import", table="devise", description="Data import cron executed").save()
    return JsonResponse(data, safe=False)

def cron_periode_comptable(request):
    data = create_periode_comptable()

    CronLog.objects.create(action="create", table="periode_comptable", description="Created accounting period succefully").save()
    return JsonResponse(data, safe=False)
    

def cron_compagnie(request):
    data = veos.get_compagnie_lists()

    CronLog.objects.create(action="import", table="compagnie", description="Data import cron executed").save()
    return JsonResponse(data, safe=False)


def cron_client():
    data = veos.get_clients_lists()

    CronLog.objects.create(action="import", table="client", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)

def cron_client_m(request):
    data = veos.get_clients_lists()

    CronLog.objects.create(action="import", table="client", description="Data import cron executed -m").save()

    return JsonResponse(data, safe=False)



def cron_police():
    data = veos.get_polices_lists()

    CronLog.objects.create(action="import", table="police", description="Data import cron executed").save()
    return JsonResponse(data, safe=False)

def send_polices(request):
    response = veos.send_polices()

    CronLog.objects.create(action="export", table="police", description="Police sent cron executed").save()

    return JsonResponse(response, safe=False)

def cron_police_m(request):
    data = veos.get_polices_lists()

    CronLog.objects.create(action="import", table="police", description="Data import cron executed -m").save()
    return JsonResponse(data, safe=False)

def cron_formule():
    data = veos.get_formules_lists()

    CronLog.objects.create(action="import", table="formule", description="Data import cron executed").save()
    return JsonResponse(data, safe=False)

def cron_formule_m(request):
    data = veos.get_formules_lists()

    CronLog.objects.create(action="import", table="formule", description="Data import cron executed -m").save()
    return JsonResponse(data, safe=False)

def cron_aliment():
    data = veos.get_aliments_lists()

    CronLog.objects.create(action="import", table="aliment", description="Data import cron executed").save()
    return JsonResponse(data, safe=False)

def cron_aliment_m(request):
    data = veos.get_aliments_lists()

    CronLog.objects.create(action="import", table="aliment", description="Data import cron executed -m").save()
    return JsonResponse(data, safe=False)


def cron_prestataire():
    data = veos.get_prestataire_lists()

    CronLog.objects.create(action="import", table="prestataire", description="Data import cron executed").save()
    return JsonResponse(data, safe=False)


def cron_prestataire_m(request):
    data = veos.get_prestataire_lists()

    CronLog.objects.create(action="import", table="prestataire", description="Data import cron executed -m").save()
    return JsonResponse(data, safe=False)

def cron_prescripteur():
    data = veos.get_prescripteurs_lists()

    CronLog.objects.create(action="import", table="prescripteur", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)


def cron_prescripteur_m(request):
    data = veos.get_prescripteurs_lists()

    CronLog.objects.create(action="import", table="prescripteur", description="Data import cron executed -m").save()

    return JsonResponse(data, safe=False)

def cron_specialite(request):
    data = veos.get_specialites_lists()

    CronLog.objects.create(action="import", table="specialite", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)

def cron_sinistre():
    data = veos.get_sinistres_lists()

    CronLog.objects.create(action="import", table="sinistre", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)

def cron_sinistre_m(request):
    data = veos.get_sinistres_lists()

    CronLog.objects.create(action="import", table="sinistre", description="Data import cron executed -m").save()

    return JsonResponse(data, safe=False)


def cron_create_sinistre():
    response = veos.cron_create_sinistre()
    CronLog.objects.create(action="send", table="sinistre", description="Send sinistres to veos").save()
    pass



def cron_acte(request):
    data = veos.get_actes_lists()

    CronLog.objects.create(action="import", table="acte", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)


def cron_photo_m(request, numero_police=None):
    data = veos.get_photos_lists(numero_police)

    CronLog.objects.create(action="import", table="photo", description="Data import cron executed").save()

    return JsonResponse(data, safe=False)


def cron_backgroundrequesttask(request):
    CronLog.objects.create(action="export", table="background_query_task",
                           description="Background request task cron executed").save()
    send_notification_background_task_mail('a.tissi@inov.africa', None)
    # load_backgroound_request_task()
    # return JsonResponse({"message": "Background request task cron executed"}, safe=False)



def send_sinistres(request):
    response = veos.send_sinistres()
    CronLog.objects.create(action="export", table="sinistre", description="Sinistres sent cron executed").save()

    return JsonResponse(response, safe=False)


def send_quittances(request):
    response = veos.send_quittances()
    CronLog.objects.create(action="export", table="quittance", description="Quittances sent cron executed").save()

    return JsonResponse(response, safe=False)


def cron_vue_quittances():
    data = veos.updt_mvquittances()

    CronLog.objects.create(action="import", table="quittance", description="Quittances import to view cron executed").save()

    return JsonResponse(data, safe=False)


def cron_vue_quittances_m(request):
    data = veos.updt_mvquittances()

    CronLog.objects.create(action="import", table="quittance", description="Quittances import to view cron executed - m").save()

    return JsonResponse(data, safe=False)


def send_clients_to_veos(request):
    data = veos.send_list_clients_to_veos()

    CronLog.objects.create(action="create", table="clients", description="Clients synchronisation V2 to VEOS cron executed " + str(data)).save()

    return JsonResponse(data, safe=False)


def send_clients_to_veos(request):
    data = veos.send_list_clients_to_veos()

    CronLog.objects.create(action="create", table="clients", description="Clients synchronisation V2 to VEOS cron executed " + str(data)).save()

    return JsonResponse(data, safe=False)


def cron_alerte_consommation():
    data = alert_consumption()

    CronLog.objects.create(action="alert_mail", table="noname",
                           description="Alerte mail suivi de consommation garant").save()

    return JsonResponse(data, safe=False)


def cron_import_sinistre():
    data = import_sinistre_manuellement_cron()

    CronLog.objects.create(action="cron_sinistre", table="noname",
                           description="cron_sinistre").save()

    return JsonResponse(data, safe=False)


def cron_get_clients_from_veos():
    data = veos.get_clients_from_veos()
    #dd(data)
    CronLog.objects.create(action="import", table="client", description="Import Clients synchronisation V2 from VEOS cron executed " + str(data)).save()

    return JsonResponse(data, safe=False)

def cron_get_clients_from_veos_m(request):
    data = veos.get_clients_from_veos()
    #dd(data)

    CronLog.objects.create(action="import", table="client", description="Import Clients synchronisation V2 from VEOS cron executed -m " + str(data)).save()

    return JsonResponse(data, safe=False)