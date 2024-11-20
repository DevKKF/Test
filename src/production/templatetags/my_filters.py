import base64
import datetime
from pprint import pprint
from decimal import Decimal
from datetime import datetime, timezone, timedelta

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from num2words import num2words

register = template.Library()

@register.filter
def money_field(montant):
    if montant == "" or montant is None: montant = 0
    money = intcomma(int(montant))
    money = money.replace(',', ' ')# remplacer la virgule quand le systeme est anglais
    return money

@register.filter
def round_value(value, decimal_places=0):
    """Arrondit la valeur à un certain nombre de décimales."""
    try:
        return round(float(value), decimal_places)
    except (ValueError, TypeError):
        return value  # En cas d'erreur, retourner la valeur sans modification 


@register.filter
def multiply(a, b):
    return a * b

@register.filter
def diviser(a, b):
    return a / b

@register.filter
def today_utc():
    return datetime.datetime.now(tz=datetime.timezone.utc)

@register.filter(name='subtract')
def subtract(value, arg):
    if value is not None and arg is not None:
        return Decimal(value) - Decimal(arg)
    else:
        return value

@register.filter(name='addition')
def addition(value, arg):
    value = value if value is not None else 0
    arg = arg if arg is not None else 0
    return value + arg

@register.filter
def with_user(total_part_compagnie_medicament, user):
    return total_part_compagnie_medicament(user)



@register.filter
def truncate_last_word(value, max_length):
    """
    Truncate a string to a maximum length, keeping the last word intact.
    """
    if len(value) <= max_length:
        return value

    # Split the string into words
    words = value.split()

    # Join all words except the last one
    truncated_text = ' '.join(words[:-1])

    # Add an ellipsis to indicate that the text has been truncated
    truncated_text += '...'

    return truncated_text


@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def entry_num_array(List):
    return range(len(List))


@register.filter
def replace_espace(value):
    return value.replace(' ', '-')

@register.filter
def replace_custom(value, arg):
    return value.replace(arg, '-')


@register.filter
def date_heure_locale(date_heure_gmt, fuseau_horaire):
    dhl = date_heure_gmt + timedelta(hours=fuseau_horaire)
    return dhl


# code pour éviter erreur (fuseau horaire tunisien{GMT+1}) : [ unsupported type for timedelta hours component: NoneType ]

#   @register.filter
#   def date_heure_locale(date_heure_gmt, fuseau_horaire):
#       if fuseau_horaire is None:
#           return date_heure_gmt
#       dhl = date_heure_gmt + timedelta(hours=fuseau_horaire)
#       return dhl

@register.filter
def nombre_en_lettre(nombre):
    try:
        return num2words(nombre, lang='fr')
    except Exception as e:
        return ''


@register.filter
def subdiviser_mots(chaine, longueur=10):

    if chaine is None or chaine == "":
        return ""
    # Séparer la chaîne en mots
    mots = chaine.split()
    
    # Liste pour stocker les résultats
    resultat = []
    
    for mot in mots:
        # Si le mot est plus long que 'longueur', le subdiviser
        if len(mot) > longueur:
            segments = [mot[i:i+longueur] for i in range(0, len(mot), longueur)]
            resultat.append(' '.join(segments))
        else:
            # Ajouter le mot tel quel s'il est plus court ou égal à 'longueur'
            resultat.append(mot)
    
    # Reconstituer la chaîne avec des espaces entre les mots
    return ' '.join(resultat)


@register.filter(name='to_base64')
def to_base64(file):
    try:
        # Lire le fichier binaire
        print('file.path')
        print(file.path)
        value = open(file.path, 'rb')
        print('value')
        print(value)
        fichier_binaire = value.read()
        # Encoder en base64
        fichier_base64 = base64.b64encode(fichier_binaire)
        # Retourner en tant que chaîne (utf-8)
        return fichier_base64.decode('utf-8')
    except Exception as e:
        return ''  # Retourne une chaîne vide si quelque chose échoue