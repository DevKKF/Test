# from msilib.schema import Property
import datetime
from datetime import date
from pprint import pprint
from django.utils import timezone

from django.db import models
from django.db.models import Q
from django.utils.safestring import mark_safe
from django_dump_die.middleware import dd
from django.db.models import F, ExpressionWrapper, DurationField

from configurations.helper_config import execute_query
from configurations.models import Banque, Bureau, Civilite, Compagnie, Fractionnement, ModeReglement, \
    Regularisation, Territorialite, TicketModerateur, User, Langue, Pays, Produit, TypeClient, TypePersonne, \
    QualiteBeneficiaire, TypeAssurance, Devise, Profession, ModeCalcul, Taxe, Apporteur, BaseCalcul, TypeQuittance, \
    NatureQuittance, TypeCarosserie, CategorieVehicule, MarqueVehicule, NatureOperation, Prestataire, TypeTarif, Acte, \
    Rubrique, Periodicite, RegroupementActe, SousRubrique, TypePrefinancement, ReseauSoin, CompteTresorerie, \
    SousRegroupementActe, Secteur, GroupeInter, BusinessUnit
from shared.enum import Genre, Statut, StatutRelation, StatutFamilial, OptionYesNo, PlacementEtGestion, \
    ModeRenouvellement, TypeEncaissementCommission, TypeMajorationContrat, CalculTM, StatutContrat, StatutPolice, StatutQuittance, \
    StatutReversementCompagnie, StatutReglementApporteurs, StatutEncaissementCommission, Energie, StatutSinistre, \
    StatutValidite, StatutIncorporation, StatutTraitement


# Create your models here.

class Monnaie(models.Model):
    code = models.CharField(max_length=5, blank=False, null=False)
    libelle = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'monnaies'
        verbose_name = 'Monnaie'
        verbose_name_plural = 'Monnaies'



def upload_location_client(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return 'clients/logos/%s.%s' % (file_name, extension)



class SecteurActivite(models.Model):
    libelle = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.libelle


    class Meta:
        db_table = 'secteur_activite'
        verbose_name = 'Secteur d\'activité '
        verbose_name_plural = 'Secteur d\'activité'

class Client(models.Model):
    veos_assure_sante_idper = models.CharField(max_length=100, blank=False, null=True)
    veos_client_idper = models.CharField(max_length=100, blank=False, null=True)
    bureau = models.ForeignKey(Bureau, on_delete=models.RESTRICT)
    type_personne = models.ForeignKey(TypePersonne, blank=False, null=True, on_delete=models.RESTRICT)
    type_client = models.ForeignKey(TypeClient, blank=False, null=True, on_delete=models.RESTRICT)
    pays = models.ForeignKey(Pays, blank=True, null=True, on_delete=models.RESTRICT)
    groupe_international = models.ForeignKey(GroupeInter, blank=True, null=True, on_delete=models.RESTRICT)
    business_unit = models.ForeignKey(BusinessUnit, blank=True, null=True, on_delete=models.RESTRICT)
    code = models.CharField(max_length=25, blank=False, null=True)
    code_provisoire = models.CharField(max_length=25, blank=False, null=True)
    nom = models.CharField(max_length=100, blank=False, null=True)
    prenoms = models.CharField(max_length=100, blank=True, null=True)
    civilite = models.ForeignKey(Civilite, blank=True, null=True, on_delete=models.RESTRICT)
    sexe = models.fields.CharField(choices=Genre.choices, max_length=1, null=True)
    date_naissance = models.DateField(blank=True, null=True, )
    telephone_mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone_fixe = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    langue = models.ForeignKey(Langue, blank=False, null=True, on_delete=models.RESTRICT)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    adresse_postale = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    gestionnaire = models.ForeignKey(User, related_name='gestionnaire_client', blank=True, null=True, on_delete=models.RESTRICT)
    site_web = models.URLField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    secteur_activite = models.ForeignKey(SecteurActivite, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    ancienne_ref = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_location_client, null=True, blank=True, )
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True)
    statut_relation = models.fields.CharField(choices=StatutRelation.choices, default=StatutRelation.PROSPECT, max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.RESTRICT)


    def __str__(self):
        if self.prenoms is None:
            self.prenoms = ''
        return f'{self.nom} {self.prenoms} ({self.code})'

    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'



class Police(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, related_name="police_updated_by", null=True, on_delete=models.RESTRICT)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.RESTRICT)
    type_assurance = models.ForeignKey(TypeAssurance, on_delete=models.RESTRICT)
    #
    bureau = models.ForeignKey(Bureau, on_delete=models.RESTRICT)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.RESTRICT)
    client = models.ForeignKey(Client, related_name='polices', on_delete=models.RESTRICT)
    veos_code_client = models.CharField(max_length=50, null=True, blank=True)
    veos_code_cie = models.CharField(max_length=50, null=True, blank=True)
    veos_id_npol = models.CharField(max_length=50, null=True, blank=True)
    veos_id_pol = models.CharField(max_length=50, null=True, blank=True)
    devise = models.ForeignKey(Devise, null=True, on_delete=models.RESTRICT)
    taxes = models.ManyToManyField(Taxe, through='TaxePolice')
    intermediaires = models.ManyToManyField(Apporteur, through='ApporteurPolice')

    apporteur = models.CharField(choices=OptionYesNo.choices, max_length=3, null=True)#False
    programme_international = models.CharField(choices=OptionYesNo.choices, max_length=3, null=True)#False
    placement_gestion = models.CharField(choices=PlacementEtGestion.choices, max_length=50, null=True)#False


    date_souscription = models.DateField(null=True)
    date_debut_effet = models.DateField()
    date_fin_effet = models.DateField()
    date_fin_police = models.DateField(null=True)
    preavis_de_resiliation = models.CharField(max_length=50, null=True)#False
    mode_renouvellement = models.CharField(choices=ModeRenouvellement.choices, max_length=50, null=True)#False

    fractionnement = models.ForeignKey(Fractionnement, on_delete=models.RESTRICT, null=True)#False
    mode_reglement = models.ForeignKey(ModeReglement, on_delete=models.RESTRICT, null=True)#False
    regularisation = models.ForeignKey(Regularisation, on_delete=models.RESTRICT, null=True)#False
    date_prochaine_facture = models.DateField(null=True)

    taux_com_courtage = models.FloatField(null=True, )
    taux_com_courtage_terme = models.FloatField(null=True, )
    taux_com_gestion = models.FloatField(null=True, )
    participation = models.CharField(choices=OptionYesNo.choices, max_length=3, null=True)#False
    taux_participation = models.IntegerField(null=True, blank=True)

    prime_ht = models.BigIntegerField(null=True)
    prime_ttc = models.BigIntegerField(null=True)
    prime_net = models.BigIntegerField(null=True)
    commission_gestion = models.BigIntegerField(null=True)
    commission_courtage = models.BigIntegerField(null=True)
    commission_intermediaires = models.BigIntegerField(null=True)
    commission_annuelle = models.BigIntegerField(null=True)
    cout_police_compagnie = models.BigIntegerField(null=True)
    cout_police_courtier = models.BigIntegerField(null=True)
    taxe = models.BigIntegerField(null=True)
    autres_taxes = models.BigIntegerField(null=True)

    type_prefinancement = models.ForeignKey(TypePrefinancement, null=True, on_delete=models.RESTRICT)
    ticket_moderateur = models.ForeignKey(TicketModerateur, null=True, on_delete=models.RESTRICT)
    mode_calcul = models.ForeignKey(ModeCalcul, null=True, on_delete=models.RESTRICT)
    #champs pour prime par famille
    prime_famille = models.IntegerField(null=True)
    nombre_max_personne_famille = models.IntegerField(null=True)
    nombre_max_enfants_famille = models.IntegerField(null=True)
    age_max_adultes = models.IntegerField(null=True)
    age_max_enfants = models.IntegerField(null=True)
    surprime_personne_sup = models.IntegerField(null=True)
    surprime_enfant_sup = models.IntegerField(null=True)
    surprime_age_adulte = models.IntegerField(null=True)
    surprime_ascendant = models.IntegerField(null=True)

    #champs pour prime par personne
    prime_personne = models.IntegerField(null=True)

    # champs pour prime adulte/enfant
    prime_adulte = models.IntegerField(null=True)
    prime_enfant = models.IntegerField(null=True)

    # champs pour prime proportionnelle
    taux_cotisation = models.IntegerField(null=True)
    part_employeur = models.IntegerField(null=True)
    cotisation_minimale = models.IntegerField(null=True)
    cotisation_maximale = models.IntegerField(null=True)

    type_majoration = models.CharField(choices=TypeMajorationContrat.choices, default='', max_length=50, null=True)

    autofinancement = models.CharField(choices=OptionYesNo.choices, default='', max_length=3, null=True)
    calcul_tm = models.CharField(choices=CalculTM.choices, default='', max_length=50, null=True)

    numero = models.CharField(max_length=50, null=True, blank=True)
    numero_provisoire = models.CharField(max_length=50, null=True, blank=True)

    taux_charge = models.FloatField(null=True)
    coefficient_n = models.FloatField(null=True)
    coefficient_n1 = models.FloatField(null=True)
    coefficient_n2 = models.FloatField(null=True)
    coefficient_n3 = models.FloatField(null=True)

    observation = models.CharField(max_length=255, null=True)

    logo_partenaire = models.ImageField(upload_to='clients/polices/logos_partenaires/', blank=True, null=True)

    statut_contrat = models.fields.CharField(choices=StatutContrat.choices, default=StatutContrat.PROJET, max_length=15, null=True)
    statut = models.fields.CharField(choices=StatutPolice.choices, default=StatutPolice.ACTIF, max_length=15, null=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.numero}'

    def save(self, *args, **kwargs):
        type_assurance_olea_sante = TypeAssurance.objects.get(id=1)
        self.type_assurance = type_assurance_olea_sante
        super(Police, self).save(*args, **kwargs)

    class Meta:
        db_table = 'polices'
        verbose_name = 'Police'
        verbose_name_plural = 'Polices'

        permissions = [
            ("can_do_create_police", "Peut créer une police"),
            ("can_do_update_police", "Peut modifier une police"),
            ("can_view_polices", "Peut afficher les polices"),
            ("can_do_avenants_polices", "Peut faire des avenants sur une police"),
        ]

    @property
    def duree_police_en_mois(self):
        duree_police = Police.objects.filter(id=self.id).annotate(
            duree_police_en_mois=ExpressionWrapper(
                F('date_fin_effet') - F('date_debut_effet'),
                output_field=DurationField()
            )
        ).values('id', 'duree_police_en_mois').first()['duree_police_en_mois']

        nombre_total_mois = duree_police.days // 30

        return nombre_total_mois


    @property
    def is_echue(self):
        last_mouvement_avenant = MouvementPolice.objects.filter(police_id=self.id, statut_validite=StatutValidite.VALIDE).filter(Q(motif__code='AN') | Q(motif__code='RENOUV')).latest('id')

        today = datetime.datetime.now(tz=timezone.utc).date()
        if last_mouvement_avenant:
            return (last_mouvement_avenant.date_fin_periode_garantie < today)
        else:
            return False

    @property
    def has_beneficiaires(self):
        return AlimentFormule.objects.filter(formule__police=self, statut=Statut.ACTIF).exists()


    @property
    def formules(self):
        try:
            formules = FormuleGarantie.objects.filter(police_id=self.id, statut=Statut.ACTIF)

            return formules

        except :
            return None


    @property
    def periode_couverture_encours(self, date_survenance=None):
        #Ajouter date_survenance - quand les sinistres seront saisi par les gestionnaires
        try:
            periode_couverture = PeriodeCouverture.objects.filter(police_id=self.id, statut_validite=StatutValidite.VALIDE).latest('id') #remplacer statut=ACTIF par statut_validite=VALIDE

            return periode_couverture

        except PeriodeCouverture.DoesNotExist:
            return None



    def periode_couverture_encours_atdate(self, date_prise_en_charge=None):
        #Ajouter date_survenance - quand les sinistres seront saisi par les gestionnaires
        pprint("TEST____________")
        pprint("date_prise_en_charge")
        pprint(date_prise_en_charge)
        print(date_prise_en_charge)
        try:

            query = Q(police_id=self.id, date_debut_effet__date__lte=date_prise_en_charge) & (Q(date_fin_effet__isnull=True) | Q(date_fin_effet__date__gte=date_prise_en_charge))

            periode_couverture = PeriodeCouverture.objects.filter(statut_validite=StatutValidite.VALIDE).filter(query).latest('id') #remplacer statut=ACTIF par statut_validite=VALIDE

            pprint("periode_couverture")
            pprint(periode_couverture)
            pprint(periode_couverture.pk)

            return periode_couverture

        except PeriodeCouverture.DoesNotExist:
            return None


    @property
    def avenant_encours(self, date_du_jour=None):
        date_du_jour = timezone.now().date()

        #date_du_jour = datetime.datetime.now(tz=timezone.utc).date()
        pprint("date_du_jour")
        pprint(date_du_jour)
        #try:

        query_cdt_dates = Q(date_effet__lte=date_du_jour) & (Q(date_fin_periode_garantie__isnull=True) | Q(date_fin_periode_garantie__gte=date_du_jour))

        mouvement_avenants = MouvementPolice.objects.filter(police_id=self.id, statut_validite=StatutValidite.VALIDE).filter(Q(motif__code='AN') | Q(motif__code='RENOUV'))#
        if len(mouvement_avenants) >1:
            mouvement_avenants.filter(query_cdt_dates)

        mouvement_avenant = mouvement_avenants.latest('id')

        pprint("mouvement_avenant")
        pprint(len(mouvement_avenants))

        return mouvement_avenant

        #except MouvementPolice.DoesNotExist:
        #    return None


    @property
    def etat_police(self):
        #tenir compte de la date du jour pour déterminer l'état de la police
        #today = datetime.datetime.now(tz=timezone.utc).date()
        today = timezone.now().date()

        mouvement = MouvementPolice.objects.filter(police_id=self.id, date_effet__lte=today, statut_validite=StatutValidite.VALIDE).order_by('-id').first()

        if mouvement:
            return mouvement.motif.etat_police
        else:
            return "En attente"

    #Déterminer l'état de la police au moment ou la pec a eu lieu
    def etat_police_atdate(self, date_prise_en_charge=None):
        #tenir compte de la date du jour pour déterminer l'état de la police
        today = datetime.datetime.now(tz=timezone.utc).date()
        mouvement = MouvementPolice.objects.filter(police_id=self.id, date_effet__lte=date_prise_en_charge, statut_validite=StatutValidite.VALIDE).order_by('-id').first()

        if mouvement:
            return mouvement.motif.etat_police
        else:
            return "En attente"


    @property
    def nombre_total_beneficiaires(self):
        today = timezone.now().date()
        police_id = self.pk

        db_query ="SELECT count(*) as nombre_beneficiaire from aliments inner join aliment_formule on aliment_formule.aliment_id = aliments.id inner join formulegarantie ON formulegarantie.id = aliment_formule.formule_id inner join polices on polices.id = formulegarantie.police_id where aliments.statut_incorporation='INCORPORE' and aliment_formule.statut_validite='VALIDE' and aliment_formule.id = ( select MAX(id) from aliment_formule WHERE aliment_id = aliments.id and statut_validite='VALIDE') and polices.id = " + str(police_id)
        db_query ="SELECT count(*) as nombre_beneficiaire from aliments inner join aliment_formule on aliment_formule.aliment_id = aliments.id inner join formulegarantie ON formulegarantie.id = aliment_formule.formule_id inner join polices on polices.id = formulegarantie.police_id where aliment_formule.statut_validite='VALIDE' and aliment_formule.id = ( select MAX(id) from aliment_formule WHERE aliment_id = aliments.id and statut_validite='VALIDE') and polices.id = " + str(police_id)
        pprint("db_query")
        print(db_query)

        data, columns = execute_query(db_query)

        final_data = []
        for row in data:
            final_data.append(dict(zip(columns, row)))

        nombre_total = final_data[0]["nombre_beneficiaire"]

        # aliment_formule_ids = AlimentFormule.objects.filter(formule_id__in=[p.id for p in self.formules], 
        #                                                     statut=Statut.ACTIF).values_list('aliment_id', 
        #                                                                                      flat=True).order_by('-id')

        # nombre_total = Aliment.objects.filter(id__in=aliment_formule_ids).count()

        return nombre_total


    @property
    def nombre_beneficiaires_entree_encours(self):
        today = timezone.now().date()
        nombre_entree_encours = MouvementAliment.objects.filter(police_id=self.id, mouvement__code="DMD-INCORPO-GRH",
                                                        date_effet__lte=today, statut_validite=StatutValidite.VALIDE,
                                                        statut_traitement=StatutTraitement.NON_TRAITE).count()

        #   print(f'@@ nombre_beneficiaires_entree_encours : {nombre_entree_encours} ')

        return nombre_entree_encours


    @property
    def nombre_beneficiaires_entres(self):
        
        nombre_entres = self.nombre_total_beneficiaires - self.nombre_beneficiaires_entree_encours - self.nombre_beneficiaires_sortis - self.nombre_beneficiaires_suspendus
 
        #   print(f'@@ nombre_entres : {nombre_entres} ')
 
        return nombre_entres


    @property
    def nombre_beneficiaires_suspendus(self):
        today = timezone.now().date()
        #   nombre_suspendus = MouvementAliment.objects.filter(police_id=self.id, mouvement__code="SUSPENSION-BENEF", date_effet__lte=today, statut_validite=StatutValidite.VALIDE).count()

        nombre_suspendus = MouvementAliment.objects.filter(
            Q(police_id=self.id, mouvement__code="SUSPENSION-BENEF", date_effet__lte=today, statut_validite=StatutValidite.VALIDE) &
            ~Q(aliment_id__in=MouvementAliment.objects.filter(
                police_id=self.id, mouvement__code="REMISEVIGUEUR-BENEF", date_effet__lte=today, statut_validite=StatutValidite.VALIDE
            ).values_list('aliment_id', flat=True))
        ).count()

        #   print(f'@@ nombre_suspendus : {nombre_suspendus} ')

        return nombre_suspendus


    @property
    def nombre_beneficiaires_sortis_encours(self):

        today = datetime.datetime.now(tz=timezone.utc).date()
        nombre_sortis_en_cours = MouvementAliment.objects.filter(police_id=self.id, mouvement__code="DMDSORTIE", date_effet__lte=today, statut_validite=StatutValidite.VALIDE, statut_traitement=StatutTraitement.NON_TRAITE).count()

        #   print(f'@@ nombre_sortis_en_cours : {nombre_sortis_en_cours} ')

        return nombre_sortis_en_cours


    @property
    def nombre_beneficiaires_sortis(self):
        #today = datetime.datetime.now(tz=timezone.utc).date()
        #nombre_sortis = MouvementAliment.objects.filter(police_id=self.id, mouvement__code="SORTIE-BENEF", date_effet__lte=today, statut_validite=StatutValidite.VALIDE).count()

        today = timezone.now().date()
        police_id = self.pk

        db_query = "SELECT count(*) as nombre_beneficiaire from aliments inner join aliment_formule on aliment_formule.aliment_id = aliments.id inner join formulegarantie ON formulegarantie.id = aliment_formule.formule_id inner join polices on polices.id = formulegarantie.police_id where aliment_formule.statut_validite='VALIDE' and aliment_formule.id = ( select MAX(id) from aliment_formule WHERE aliment_id = aliments.id and statut_validite='VALIDE') and polices.id = " + str(police_id) + " and aliments.date_sortie IS NOT NULL and aliments.date_sortie <= '" + str(today) + "'"
        pprint("db_query")
        print(db_query)

        data, columns = execute_query(db_query)

        final_data = []
        for row in data:
            final_data.append(dict(zip(columns, row)))

        nombre_sortis = final_data[0]["nombre_beneficiaire"]

        #   print(f'@@ nombre_sortis : {nombre_sortis} ')

        return nombre_sortis


class HistoriquePolice(models.Model):
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)

    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, related_name="historique_police_updated_by", null=True, on_delete=models.RESTRICT)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.RESTRICT)
    type_assurance = models.ForeignKey(TypeAssurance, on_delete=models.RESTRICT)
    #
    bureau = models.ForeignKey(Bureau, on_delete=models.RESTRICT)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.RESTRICT)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    veos_code_client = models.CharField(max_length=50, null=True, blank=True)
    veos_code_cie = models.CharField(max_length=50, null=True, blank=True)
    veos_id_npol = models.CharField(max_length=50, null=True, blank=True)
    veos_id_pol = models.CharField(max_length=50, null=True, blank=True)
    devise = models.ForeignKey(Devise, null=True, on_delete=models.RESTRICT)
    taxes = models.ManyToManyField(Taxe, through='HistoriqueTaxePolice')
    intermediaires = models.ManyToManyField(Apporteur, through='HistoriqueApporteurPolice')

    apporteur = models.CharField(choices=OptionYesNo.choices, max_length=3, null=True)#False
    programme_international = models.CharField(choices=OptionYesNo.choices, max_length=3, null=True)#False
    placement_gestion = models.CharField(choices=PlacementEtGestion.choices, max_length=50, null=True)#False


    date_souscription = models.DateField(null=True)
    date_debut_effet = models.DateField()
    date_fin_effet = models.DateField()
    date_fin_police = models.DateField(null=True)
    preavis_de_resiliation = models.CharField(max_length=50, null=True)#False
    mode_renouvellement = models.CharField(choices=ModeRenouvellement.choices, max_length=50, null=True)#False

    fractionnement = models.ForeignKey(Fractionnement, on_delete=models.RESTRICT, null=True)#False
    mode_reglement = models.ForeignKey(ModeReglement, on_delete=models.RESTRICT, null=True)#False
    regularisation = models.ForeignKey(Regularisation, on_delete=models.RESTRICT, null=True)#False
    date_prochaine_facture = models.DateField(null=True)

    taux_com_courtage = models.FloatField(null=True, )
    taux_com_courtage_terme = models.FloatField(null=True, )
    taux_com_gestion = models.FloatField(null=True, )
    participation = models.CharField(choices=OptionYesNo.choices, max_length=3, null=True)#False
    taux_participation = models.IntegerField(null=True, blank=True)

    prime_ht = models.BigIntegerField(null=True)
    prime_ttc = models.BigIntegerField(null=True)
    prime_net = models.BigIntegerField(null=True)
    commission_gestion = models.BigIntegerField(null=True)
    commission_courtage = models.BigIntegerField(null=True)
    commission_intermediaires = models.BigIntegerField(null=True)
    commission_annuelle = models.BigIntegerField(null=True)
    cout_police_compagnie = models.BigIntegerField(null=True)
    cout_police_courtier = models.BigIntegerField(null=True)
    taxe = models.BigIntegerField(null=True)
    autres_taxes = models.BigIntegerField(null=True)

    type_prefinancement = models.ForeignKey(TypePrefinancement, null=True, on_delete=models.RESTRICT)
    ticket_moderateur = models.ForeignKey(TicketModerateur, null=True, on_delete=models.RESTRICT)
    mode_calcul = models.ForeignKey(ModeCalcul, null=True, on_delete=models.RESTRICT)
    #champs pour prime par famille
    prime_famille = models.IntegerField(null=True)
    nombre_max_personne_famille = models.IntegerField(null=True)
    nombre_max_enfants_famille = models.IntegerField(null=True)
    age_max_adultes = models.IntegerField(null=True)
    age_max_enfants = models.IntegerField(null=True)
    surprime_personne_sup = models.IntegerField(null=True)
    surprime_enfant_sup = models.IntegerField(null=True)
    surprime_age_adulte = models.IntegerField(null=True)
    surprime_ascendant = models.IntegerField(null=True)

    #champs pour prime par personne
    prime_personne = models.IntegerField(null=True)

    # champs pour prime adulte/enfant
    prime_adulte = models.IntegerField(null=True)
    prime_enfant = models.IntegerField(null=True)

    # champs pour prime proportionnelle
    taux_cotisation = models.IntegerField(null=True)
    part_employeur = models.IntegerField(null=True)
    cotisation_minimale = models.IntegerField(null=True)
    cotisation_maximale = models.IntegerField(null=True)

    type_majoration = models.CharField(choices=TypeMajorationContrat.choices, default='', max_length=50, null=True)

    autofinancement = models.CharField(choices=OptionYesNo.choices, default='', max_length=3, null=True)
    calcul_tm = models.CharField(choices=CalculTM.choices, default='', max_length=50, null=True)

    numero = models.CharField(max_length=50, null=True, blank=True)
    numero_provisoire = models.CharField(max_length=50, null=True, blank=True)

    taux_charge = models.FloatField(null=True)
    coefficient_n = models.FloatField(null=True)
    coefficient_n1 = models.FloatField(null=True)
    coefficient_n2 = models.FloatField(null=True)
    coefficient_n3 = models.FloatField(null=True)

    observation = models.CharField(max_length=255, null=True)

    logo_partenaire = models.ImageField(upload_to='clients/polices/logos_partenaires/', blank=True, null=True)

    statut_contrat = models.fields.CharField(choices=StatutContrat.choices, default=StatutContrat.PROJET, max_length=15, null=True)
    statut = models.fields.CharField(choices=StatutPolice.choices, default=StatutPolice.ACTIF, max_length=15, null=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.numero}'

    class Meta:
        db_table = 'historique_polices'
        verbose_name = 'Historique Police'
        verbose_name_plural = 'Historiques Polices'


class PoliceClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)
    observation = models.CharField(max_length=255, null=True, blank=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'client_police'
        verbose_name = 'Client police'
        verbose_name_plural = 'Clients-polices'


class PeriodeCouverture(models.Model):
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    date_debut_effet = models.DateTimeField(blank=True, null=True)
    date_fin_effet = models.DateTimeField(blank=True, null=True)
    observation = models.CharField(max_length=255, null=True, blank=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True, blank=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Période {self.date_debut_effet} - {self.date_fin_effet}'

    class Meta:
        db_table = 'periode_couverture'
        verbose_name = 'Période de couverture'
        verbose_name_plural = 'Périodes de couverture'


#Indique si TPG ou TPP
class ModePrefinancement(models.Model):
    code = models.CharField(max_length=5, null=True, blank=True)
    libelle = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'mode_prefinancement'
        verbose_name = 'Mode de prefinancement'
        verbose_name_plural = 'Modes de prefinancement'


class FormuleGarantie(models.Model):
    mode_prefinancement = models.ForeignKey(ModePrefinancement, null=True, on_delete=models.RESTRICT)
    reseau_soin = models.ForeignKey(ReseauSoin, null=True, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, related_name="fg_updated_by", null=True, on_delete=models.RESTRICT)
    deleted_by = models.ForeignKey(User, related_name="fg_deleted_by", null=True, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, on_delete=models.RESTRICT, null=True)
    bureau = models.ForeignKey(Bureau, on_delete=models.RESTRICT, null=True)
    territorialite = models.ForeignKey(Territorialite, on_delete=models.RESTRICT, null=True)
    type_tarif = models.ForeignKey(TypeTarif, on_delete=models.RESTRICT, null=True)
    libelle = models.CharField(max_length=100, blank=True, null=True)
    exclusion = models.TextField(max_length=250, blank=True, null=True)  # New text field

    # Champs complementaires
    infos_carte_consultation = models.CharField(max_length=100, blank=True, null=True)
    infos_carte_hospitalisation = models.CharField(max_length=100, blank=True, null=True)
    infos_carte_ambulatoire = models.CharField(max_length=100, blank=True, null=True)
    infos_carte_vitamine = models.CharField(max_length=100, blank=True, null=True)
    infos_carte_vaccination = models.CharField(max_length=100, blank=True, null=True)
    infos_carte_numero_police = models.CharField(max_length=100, blank=True, null=True)
    infos_carte_show_numero_police = models.BooleanField(default=True)


    garantis_pharmacie = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    taux_couverture = models.IntegerField(blank=True, null=True)
    taux_tm = models.IntegerField(blank=True, null=True)
    plafond_conso_famille = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    plafond_conso_individuelle = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'formulegarantie'
        verbose_name = 'Formule de garantie'
        verbose_name_plural = 'Formule de garantie'


#les jointures sont faibles,
# si le bareme concerne toute la police, alors uniquement la police sera renseigné, collège et qualite_beneficiaire resteront vides,
#s'il concerne un college en particulier alors college sera renseigné
class Bareme(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    deleted_by = models.ForeignKey(User, related_name="deleted_by", null=True, on_delete=models.RESTRICT)
    formulegarantie = models.ForeignKey(FormuleGarantie, on_delete=models.RESTRICT, null=True)
    rubrique = models.ForeignKey(Rubrique, on_delete=models.RESTRICT, null=True)
    sous_rubrique = models.ForeignKey(SousRubrique, on_delete=models.RESTRICT, null=True)
    regroupement_acte = models.ForeignKey(RegroupementActe, on_delete=models.RESTRICT, null=True)
    sous_regroupement_acte = models.ForeignKey(SousRegroupementActe, on_delete=models.RESTRICT, null=True)
    acte = models.ForeignKey(Acte, on_delete=models.RESTRICT, null=True)
    is_garanti = models.BooleanField(default=True)
    qualite_beneficiaire = models.ForeignKey(QualiteBeneficiaire, on_delete=models.RESTRICT, null=True)
    taux_tm = models.IntegerField(blank=True, null=True)
    taux_couverture = models.IntegerField(blank=True, null=True)
    plafond_rubrique = models.IntegerField(blank=True, null=True)
    plafond_sous_rubrique = models.IntegerField(blank=True, null=True)
    plafond_regroupement_acte = models.IntegerField(blank=True, null=True)
    plafond_sous_regroupement_acte = models.IntegerField(blank=True, null=True)
    plafond_acte = models.IntegerField(blank=True, null=True)
    nombre_acte = models.IntegerField(blank=True, null=True)
    periodicite = models.ForeignKey(Periodicite, on_delete=models.RESTRICT, null=True)
    unite_frequence = models.IntegerField(blank=True, null=True)
    frequence = models.IntegerField(blank=True, null=True)
    plafond_individuel = models.IntegerField(blank=True, null=True)
    plafond_famille = models.IntegerField(blank=True, null=True)
    age_minimum = models.IntegerField(blank=True, null=True)
    age_maximum = models.IntegerField(blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True)

    class Meta:
        db_table = 'bareme'
        verbose_name = 'Barème'
        verbose_name_plural = 'Barème'


class TauxCouvertureVariable(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    formulegarantie = models.ForeignKey(FormuleGarantie, on_delete=models.RESTRICT)
    secteur = models.ForeignKey(Secteur, on_delete=models.RESTRICT) #Pour une même formule, le taux de couverture varie selon le secteur (public/privé) du prestataire
    taux_couverture = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)

    def __str__(self):
        return f'{self.formulegarantie.libelle} - {self.taux_couverture} %'

    class Meta:
        db_table = 'taux_couverture_variable'
        verbose_name = "Taux de couverture"
        verbose_name_plural = "Taux de couverture"


class FormuleRubriquePrefinance(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    formulegarantie = models.ForeignKey(FormuleGarantie, on_delete=models.RESTRICT)
    rubrique = models.ForeignKey(Rubrique, null=True, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)

    def __str__(self):
        return f'{self.formulegarantie.libelle} - {self.rubrique.name}'

    class Meta:
        db_table = 'formule_rubrique_prefinance'
        verbose_name = "Rubrique préfinancé sur la formule"
        verbose_name_plural = "Rubriques préfinancés sur la formule"



def upload_location_aliment(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if filename.startswith('photo_'):
        return f'beneficiaires/photos/{filename}'
    return 'photos/%s.%s' % (file_name, extension)







class Aliment(models.Model):
    #champs pour la migration veos
    sms_active = models.BooleanField(default=False)
    veos_id_npol = models.CharField(max_length=50, null=True, blank=True)
    veos_code_aliment = models.CharField(max_length=50, blank=True, null=True)
    veos_adherent_principal = models.CharField(max_length=50, null=True, blank=True)
    veos_adherent_principal_id_per = models.CharField(max_length=50, null=True, blank=True)
    veos_code_qualite_beneficiaire = models.CharField(max_length=50, null=True, blank=True)
    veos_code_formule = models.CharField(max_length=50, null=True, blank=True)
    veos_code_college = models.CharField(max_length=50, null=True, blank=True)
    veos_numero_carte = models.CharField(max_length=50, null=True, blank=True)
    observation = models.CharField(max_length=255, null=True, blank=True)

    #
    bureau = models.ForeignKey(Bureau, null=True, on_delete=models.RESTRICT)
    adherent_principal = models.ForeignKey('self', null=True, on_delete=models.RESTRICT)
    formules = models.ManyToManyField(FormuleGarantie, through='AlimentFormule')
    qualite_beneficiaire = models.ForeignKey(QualiteBeneficiaire, null=True, on_delete=models.RESTRICT)
    civilite = models.ForeignKey(Civilite, null=True, on_delete=models.RESTRICT)
    pays_naissance = models.ForeignKey(Pays, related_name='pays_naissance', null=True, on_delete=models.RESTRICT)
    pays_residence = models.ForeignKey(Pays, related_name='pays_residence', null=True, on_delete=models.RESTRICT)
    pays_activite_professionnelle = models.ForeignKey(Pays, related_name='pays_activite_professionnelle', null=True,
                                                      on_delete=models.RESTRICT)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.RESTRICT)
    profession_libelle = models.CharField(max_length=50, blank=False, null=True)
    nom = models.CharField(max_length=50, blank=False, null=True)
    prenoms = models.CharField(max_length=50, blank=False, null=True)
    nom_jeune_fille = models.CharField(max_length=100, blank=False, null=True)
    date_naissance = models.DateField(blank=False, null=True)
    lieu_naissance = models.CharField(max_length=100, blank=False, null=True)
    genre = models.fields.CharField(choices=Genre.choices, max_length=10, null=False)
    email = models.CharField(max_length=50, blank=True, null=True)

    numero_securite_sociale = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    numero_famille = models.CharField(max_length=50, blank=True, null=True)
    numero_famille_v1 = models.CharField(max_length=50, blank=True, null=True)
    numero_ordre = models.CharField(max_length=50, blank=True, null=True)
    matricule_employe = models.CharField(max_length=50, blank=True, null=True)
    matricule_cie = models.CharField(max_length=50, blank=True, null=True)
    date_affiliation = models.DateField(blank=True, null=True)
    date_sortie = models.DateField(blank=True, null=True)
    photo = models.ImageField(max_length=255, blank=True, null=True, upload_to=upload_location_aliment)
    statut_familiale = models.fields.CharField(choices=StatutFamilial.choices, default=StatutFamilial.CHOISIR,
                                               max_length=15, null=True)
    numero_piece = models.CharField(max_length=50, blank=True, null=True)

    code_postal = models.CharField(max_length=20, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone_fixe = models.CharField(max_length=50, blank=True, null=True)
    telephone_mobile = models.CharField(max_length=50, blank=True, null=True)

    rib = models.CharField(max_length=50, blank=True, null=True)
    surprime_ht = models.BigIntegerField(null=True, blank=True)
    surprime_ttc = models.BigIntegerField(null=True, blank=True)
    plafond_extra = models.BigIntegerField(null=True, blank=True)
    apci_ald = models.CharField(max_length=50, blank=True, null=True)

    plafond_individuel = models.BigIntegerField(null=True)
    plafond_famille = models.BigIntegerField(null=True)

    commentaire = models.CharField(max_length=20, blank=True, null=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True)
    statut_incorporation = models.fields.CharField(choices=StatutIncorporation.choices, default=StatutIncorporation.INCORPORE, max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user_extranet = models.ForeignKey(User, related_name="aliments" ,null=True, on_delete=models.RESTRICT)
    numero_famille_du_mois = models.IntegerField(blank=True, null=True)
    has_photo_veos = models.BooleanField(default=True)
    statut_import_photo_veos = models.BooleanField(default=False)
    etat = models.CharField(max_length=50, blank=True, null=True)
    #formulegarantie = models.ForeignKey(FormuleGarantie, null=True, on_delete=models.RESTRICT)
    #police = models.ForeignKey(Police, null=True, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.nom} {self.prenoms}'

    class Meta:
        db_table = 'aliments'
        verbose_name = 'Aliment'
        verbose_name_plural = 'aliments'


    @property
    def age(self):
        a = 0
        if self.date_naissance:
            today = date.today()
            a = today.year - self.date_naissance.year
            pprint(self.date_naissance.year)

            if today.month < self.date_naissance.month or (today.month == self.date_naissance.month and today.day < self.date_naissance.day):
                a -= 1

        return a


    @property
    def nom_prenoms(self):
        return f'{self.nom} {self.prenoms}'


    @property
    def telephone_mobile_sans_indicatif(self):
        indicatif = self.bureau.pays.indicatif

        return self.telephone_mobile[len(indicatif):] if indicatif and self.telephone_mobile and self.telephone_mobile.startswith(indicatif) else self.telephone_mobile


    @property
    def telephone_fixe_sans_indicatif(self):
        indicatif = self.bureau.pays.indicatif

        return self.telephone_fixe[len(indicatif):] if indicatif and self.telephone_fixe and self.telephone_fixe.startswith(indicatif) else self.telephone_fixe


    def carte_active(self):
        try:
            return self.cartes.filter(statut=Statut.ACTIF).latest('id')
        except Carte.DoesNotExist:
            return ""


    def client(self):
        try:
            aliment_formule = AlimentFormule.objects.filter(aliment_id=self.id, statut=Statut.ACTIF).latest('id')
            police = aliment_formule.formule.police
            client = police.client
            return client

        except Client.DoesNotExist:
            return None


    @property
    def formules(self):
        try:
            aliment_formules = AlimentFormule.objects.filter(aliment_id=self.id)

            return aliment_formules

        except:
            return None

    @property
    def aliment_formule(self):
        try:
            aliment_formule = AlimentFormule.objects.filter(aliment_id=self.id, statut=Statut.ACTIF).latest('id')

            return aliment_formule

        except AlimentFormule.DoesNotExist:
            return None


    @property
    def formule(self, date_prise_en_charge=None):
        if date_prise_en_charge is None:
            date_prise_en_charge = datetime.datetime.now(tz=datetime.timezone.utc).date()
            # date_debut=date_prise_en_charge
            #pprint("date_prise_en_charge")
            #pprint(date_prise_en_charge)

        try:
            query = Q(aliment_id=self.id, date_debut__date__lte=date_prise_en_charge) & (Q(date_fin__isnull=True) | Q(date_fin__date__gte=date_prise_en_charge))
            aliment_formules = AlimentFormule.objects.filter(query)

            if aliment_formules:
                aliment_formule = AlimentFormule.objects.filter(query).latest('id')
                formule = aliment_formule.formule if aliment_formule else None
                return formule

            else:
                return None

        except FormuleGarantie.DoesNotExist:
            pprint("FormuleGarantie.DoesNotExist")
            return None


    #Identique à formule sauf que formule est une propriété et formuleencours une fonction
    #sera plus utilisé quand les gestionnaires vont saisir les sinistre en retards
    def formuleencours(self, date_prise_en_charge=None):
        if date_prise_en_charge is None:
            date_prise_en_charge = datetime.datetime.now(tz=datetime.timezone.utc).date()
            # date_debut=date_prise_en_charge
            pprint("La date survenance n'est pas renseigné, on considère la date du jour")

        pprint("La date survenance est renseigné")
        pprint("date_prise_en_charge")
        pprint(date_prise_en_charge)

        try:
            query = Q(aliment_id=self.id, date_debut__date__lte=date_prise_en_charge) & (Q(date_fin__isnull=True) | Q(date_fin__date__gte=date_prise_en_charge))
            aliment_formules = AlimentFormule.objects.filter(query)

            if aliment_formules:
                aliment_formule = AlimentFormule.objects.filter(query).latest('id')
                formule = aliment_formule.formule if aliment_formule else None
                return formule

            else:
                return None

        except FormuleGarantie.DoesNotExist:
            pprint("FormuleGarantie.DoesNotExist")
            return None


    #Identique à formule sauf que formule est une propriété et formuleencours une fonction
    #sera plus utilisé quand les gestionnaires vont saisir les sinistre en retards
    def formule_atdate(self, date_prise_en_charge=None):
        if date_prise_en_charge is None:
            date_prise_en_charge = datetime.datetime.now(tz=datetime.timezone.utc).date()
            # date_debut=date_prise_en_charge
            pprint("La date survenance n'est pas renseigné, on considère la date du jour")
        else:
            if isinstance(date_prise_en_charge, datetime.datetime):
                date_prise_en_charge = date_prise_en_charge.date()

        pprint("date_prise_en_charge")
        pprint(date_prise_en_charge)

        try:
            query = Q(aliment_id=self.id, date_debut__date__lte=date_prise_en_charge) & (Q(date_fin__isnull=True) | Q(date_fin__date__gte=date_prise_en_charge))
            aliment_formules = AlimentFormule.objects.filter(query)

            if aliment_formules:
                aliment_formule = AlimentFormule.objects.filter(query).latest('id')
                formule = aliment_formule.formule if aliment_formule else None

                pprint("la formule du bénéficiaire est")
                pprint(formule)

                return formule

            else:
                return None

        except FormuleGarantie.DoesNotExist:
            pprint("FormuleGarantie.DoesNotExist")
            return None


    @property
    def last_formule(self):
        query = Q(aliment_id=self.id, statut_validite=StatutValidite.VALIDE)
        aliment_formule = AlimentFormule.objects.filter(query).latest('id')

        pprint("last_formule")
        pprint(aliment_formule)
        formule = aliment_formule.formule if aliment_formule else None

        return formule
        '''
        try:
            query = Q(aliment_id=self.id)
            aliment_formule = AlimentFormule.objects.filter(query).latest('id')
            formule = aliment_formule.formule if aliment_formule else None

            return formule

        except FormuleGarantie.DoesNotExist:
            pprint("FormuleGarantie.DoesNotExist")
            return None
        '''


    @property
    def last_sinistre(self):
        # Comparaison de dates
        last_sinistre = self.ses_sinistres.all().filter(
            statut_validite=StatutValidite.VALIDE,
            statut__in=[StatutSinistre.ACCORDE, StatutSinistre.ATTENTE]
        ).order_by('-date_survenance').first()

        return last_sinistre


    @property
    def last_mouvement(self, date_reference=None):
        if date_reference is None:
            date_reference = datetime.datetime.now(tz=datetime.timezone.utc).date()

        elif isinstance(date_reference, datetime.datetime):
            date_reference = date_reference.date()

        pprint("date_reference")
        pprint(date_reference)
        if date_reference:
            last_mouvement = self.ses_mouvements.all().filter(
                date_effet__lte=date_reference,
                statut_validite=StatutValidite.VALIDE,
            ).order_by('-id').first()

        else:
            last_mouvement = None

        return last_mouvement

    @property
    def etat_beneficiaire(self, date_reference=None, police_id=None):
        #last_mouvement = self.last_mouvement(date_reference)
        if date_reference is None:
            date_reference = datetime.datetime.now(tz=datetime.timezone.utc).date()

        elif isinstance(date_reference, datetime.datetime):
            date_reference = date_reference.date()

        if date_reference:
            last_mouvement = self.ses_mouvements.all().filter(
                date_effet__lte=date_reference,
                statut_validite=StatutValidite.VALIDE,
            ).order_by('-id').first()

        else:
            last_mouvement = None

        if self.date_sortie and self.date_sortie <= date_reference:
            etat_beneficiaire = 'SORTI'

        else:
            if last_mouvement:
                code_mouvement = last_mouvement.mouvement.code
                etat_beneficiaire = last_mouvement.mouvement.libelle

                if code_mouvement == "SUSPENSION-BENEF":
                    etat_beneficiaire = "SUSPENDU"

                if code_mouvement == "SORTIE-BENEF":
                    etat_beneficiaire = "SORTI"

                if code_mouvement == "INCORPORATION" or code_mouvement == "REMISEVIGUEUR-BENEF" or code_mouvement == "CHANGEFORMULE-BENEF":
                    etat_beneficiaire = "ACTIF"

                if code_mouvement == "DMD-INCORPO-GRH":
                    etat_beneficiaire = "ENTREE EN COURS"

                if code_mouvement == "DMDSUSPENSION":
                    etat_beneficiaire = "SUSPENSION EN COURS"

                if code_mouvement == "DMDSORTIE":
                    etat_beneficiaire = "SORTIE EN COURS"


            else:
                etat_beneficiaire = "ACTIF" if self.statut_incorporation == "INCORPORE" else "ENTREE EN COURS"


        return etat_beneficiaire


    def etat_beneficiaire_atdate(self, date_reference=None, police_id=None):
        #last_mouvement = self.last_mouvement(date_reference)
        if date_reference is None:
            date_reference = datetime.datetime.now(tz=datetime.timezone.utc).date()

        elif isinstance(date_reference, datetime.datetime):
            date_reference = date_reference.date()

        if date_reference:
            if police_id:
                last_mouvement = self.ses_mouvements.all().filter(
                    date_effet__lte=date_reference,
                    statut_validite=StatutValidite.VALIDE,
                    police_id=police_id,
                ).order_by('-id').first()

            else:
                last_mouvement = self.ses_mouvements.all().filter(
                    date_effet__lte=date_reference,
                    statut_validite=StatutValidite.VALIDE,
                ).order_by('-id').first()

        else:
            last_mouvement = None

        if self.date_sortie and self.date_sortie <= date_reference:
            etat_beneficiaire = 'SORTI'

        else:
            if last_mouvement:
                code_mouvement = last_mouvement.mouvement.code
                etat_beneficiaire = last_mouvement.mouvement.libelle

                if code_mouvement == "SUSPENSION-BENEF":
                    etat_beneficiaire = "SUSPENDU"

                if code_mouvement == "SORTIE-BENEF":
                    etat_beneficiaire = "SORTI"

                if code_mouvement == "INCORPORATION" or code_mouvement == "REMISEVIGUEUR-BENEF" or code_mouvement == "CHANGEFORMULE-BENEF":
                    etat_beneficiaire = "ACTIF"

                if code_mouvement == "DMD-INCORPO-GRH":
                    etat_beneficiaire = "ENTREE EN COURS"

                if code_mouvement == "DMDSUSPENSION":
                    etat_beneficiaire = "SUSPENSION EN COURS"

                if code_mouvement == "DMDSORTIE":
                    etat_beneficiaire = "SORTIE EN COURS"

                pprint("code_mouvement")
                pprint(code_mouvement)
                pprint("etat_beneficiaire")
                pprint(etat_beneficiaire)

            else:
                etat_beneficiaire = "ACTIF" if self.statut_incorporation == "INCORPORE" else "ENTREE EN COURS"

        return etat_beneficiaire


    @property
    def police_encours(self):
        #
        aliment_formule = AlimentFormule.objects.filter(
            aliment=self,
            statut_validite=StatutValidite.VALIDE
        ).last()

        police = aliment_formule.formule.police

        return police


class PhotoIdentite(models.Model):
    aliment = models.ForeignKey(Aliment, on_delete=models.RESTRICT)
    fichier = models.ImageField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'photo'
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class AlimentFormule(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    aliment = models.ForeignKey(Aliment, related_name="historique_formules", on_delete=models.RESTRICT)
    formule = models.ForeignKey(FormuleGarantie, null=True, on_delete=models.RESTRICT)
    motif = models.CharField(max_length=255, blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True, blank=True)
    statut_validite = models.fields.CharField(choices=Statut.choices, default=StatutValidite.VALIDE, max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'aliment_formule'
        verbose_name = "Bénéficiaire d'une formule"
        verbose_name_plural = "Bénéficiaires d'un formule"



class AlimentTemporaire(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    session_import = models.CharField(max_length=255, blank=True, null=True)
    aliment = models.ForeignKey(Aliment, on_delete=models.RESTRICT)
    numero_famille_import = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'aliment_temporaire'
        verbose_name = "Aliment temporaire"
        verbose_name_plural = "Aliments temporaires"


class TaxePolice(models.Model):
    taxe = models.ForeignKey(Taxe, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    montant = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'taxe_police'
        verbose_name = 'Taxe de la police'
        verbose_name_plural = 'Taxes de la police'


class ApporteurPolice(models.Model):
    added_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    apporteur = models.ForeignKey(Apporteur, on_delete=models.RESTRICT)
    base_calcul = models.ForeignKey(BaseCalcul, on_delete=models.RESTRICT)
    taux_com_affaire_nouvelle = models.FloatField(blank=True, null=True)
    taux_com_renouvellement = models.FloatField(blank=True, null=True)
    date_effet = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=Statut.choices, default=StatutValidite.VALIDE, max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'apporteurs_police'
        verbose_name = 'Apporteur de la police'
        verbose_name_plural = 'Apporteurs de la police'

    def com_affaire_nouvelle(self):
        commission_courtage = self.police.commission_courtage/100 if self.police.commission_courtage else 0
        commission_gestion = self.police.commission_gestion/100 if self.police.commission_gestion else 0
        base_calcul_code = self.base_calcul.code

        if base_calcul_code == "COM_GEST":
            com_affaire_nouvelle = self.taux_com_affaire_nouvelle * commission_gestion

        elif base_calcul_code == "COM_COURT":
            com_affaire_nouvelle = self.taux_com_affaire_nouvelle * commission_courtage

        elif base_calcul_code == "Com Total":
            com_affaire_nouvelle = self.taux_com_affaire_nouvelle * (commission_courtage + commission_gestion)

        else:
            com_affaire_nouvelle = self.taux_com_affaire_nouvelle

        return com_affaire_nouvelle



class HistoriqueTaxePolice(models.Model):
    taxe = models.ForeignKey(Taxe, on_delete=models.RESTRICT)
    historique_police = models.ForeignKey(HistoriquePolice, on_delete=models.RESTRICT)
    montant = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'historique_taxe_police'
        verbose_name = 'Historique des taxes de la police'
        verbose_name_plural = 'Historique des taxes de la police'


class HistoriqueApporteurPolice(models.Model):
    added_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    historique_police = models.ForeignKey(HistoriquePolice, on_delete=models.RESTRICT)
    apporteur = models.ForeignKey(Apporteur, on_delete=models.RESTRICT)
    base_calcul = models.ForeignKey(BaseCalcul, on_delete=models.RESTRICT)
    taux_com_affaire_nouvelle = models.FloatField(blank=True, null=True)
    taux_com_renouvellement = models.FloatField(blank=True, null=True)
    date_effet = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=Statut.choices, default=StatutValidite.VALIDE, max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'historique_apporteurs_police'
        verbose_name = 'historique des apporteurs de la police'
        verbose_name_plural = 'historiques des apporteurs de la police'



def upload_location_carte(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if filename.startswith('qrcode_image_'):
        return f'beneficiaires/cartes_qrcodes/{filename}'
    return f'beneficiaire/cartes/{filename}'

class Carte(models.Model):
    bureau = models.ForeignKey(Bureau, null=True, on_delete=models.RESTRICT)
    aliment = models.ForeignKey(Aliment, related_name='cartes', null=True, blank=True, on_delete=models.RESTRICT)
    numero = models.CharField(unique=True, max_length=30, blank=True, null=True)
    motif_edition = models.CharField(max_length=255, blank=True, null=True)
    date_edition = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_desactivation = models.DateTimeField(blank=True, null=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    qrcode_file = models.ImageField(upload_to=upload_location_carte, blank=True, null=True)

    def __str__(self):
        return self.numero

    class Meta:
        db_table = 'cartes'
        verbose_name = 'Carte'
        verbose_name_plural = 'Cartes'


class Mouvement(models.Model):
    libelle = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'mouvements'
        verbose_name = 'Mouvement'
        verbose_name_plural = 'Mouvements'


class Motif(models.Model):
    mouvement = models.ForeignKey(Mouvement, on_delete=models.RESTRICT)
    libelle = models.CharField(max_length=50, blank=True, null=True)
    etat_police = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'motifs'
        verbose_name = 'Motif'
        verbose_name_plural = 'Motifs'

    # historique des mouvements de la police


class MouvementPolice(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    mp_deleted_by = models.ForeignKey(User, related_name="mp_deleted_by", null=True, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    mouvement = models.ForeignKey(Mouvement, on_delete=models.RESTRICT)
    motif = models.ForeignKey(Motif, on_delete=models.RESTRICT)
    observation = models.CharField(max_length=255, blank=True, null=True)
    date_effet = models.DateField(blank=True, null=True)
    date_fin_periode_garantie = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    historique_police = models.ForeignKey(HistoriquePolice, null=True, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Mouvement: {self.mouvement.libelle}/{self.motif.libelle} - Police N° {self.police.numero}'

    class Meta:
        db_table = 'mouvements_polices'
        verbose_name = 'Mouvement de la police'
        verbose_name_plural = 'Mouvements de la police'


class MouvementAliment(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    aliment = models.ForeignKey(Aliment, related_name="ses_mouvements", on_delete=models.RESTRICT)
    mouvement = models.ForeignKey(Mouvement, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, null=True, on_delete=models.RESTRICT)
    #motif = models.ForeignKey(Motif, on_delete=models.RESTRICT)
    motif = models.CharField(max_length=255, blank=True, null=True)
    date_effet = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    statut_traitement = models.fields.CharField(choices=StatutTraitement.choices, default=StatutTraitement.TRAITE, max_length=15, null=True)

    def __str__(self):
        return f'{self.mouvement.libelle} du bénéficiaire {self.aliment.nom} {self.aliment.prenoms}'

    class Meta:
        db_table = 'mouvements_aliments'
        verbose_name = "Mouvement sur l'aliment"
        verbose_name_plural = "Mouvements sur l'aliment"



class Quittance(models.Model):
    bureau = models.ForeignKey(Bureau, null=True, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    deleted_by = models.ForeignKey(User, related_name="quittance_deleted_by", null=True, on_delete=models.RESTRICT)
    type_quittance = models.ForeignKey(TypeQuittance, null=True, on_delete=models.RESTRICT)
    nature_quittance = models.ForeignKey(NatureQuittance, null=True, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, null=True, on_delete=models.RESTRICT)
    compagnie = models.ForeignKey(Compagnie, null=True, on_delete=models.RESTRICT)
    devise = models.ForeignKey(Devise, null=True, on_delete=models.RESTRICT)
    taxes = models.ManyToManyField(Taxe, through='TaxeQuittance')
    numero = models.CharField(max_length=20, unique=True, blank=True, null=True)
    prime_ht = models.BigIntegerField(null=True)
    cout_police_courtier = models.BigIntegerField(null=True)
    cout_police_compagnie = models.BigIntegerField(null=True)
    taxe = models.BigIntegerField(null=True)
    autres_taxes = models.BigIntegerField(null=True)
    prime_ttc = models.BigIntegerField(null=True)
    montant_compagnie = models.BigIntegerField(null=True)
    taux_com_gestion = models.FloatField(blank=True, default=None, null=True)
    taux_com_courtage = models.FloatField(blank=True, default=None, null=True)
    commission_courtage = models.BigIntegerField(null=True)
    commission_gestion = models.BigIntegerField(null=True)
    commission_intermediaires = models.BigIntegerField(null=True)
    montant_regle = models.BigIntegerField(null=True)
    solde = models.BigIntegerField(null=True)
    taux_euro = models.FloatField(blank=True, default=None, null=True)
    taux_usd = models.FloatField(blank=True, default=None, null=True)
    date_emission = models.DateField(blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    statut = models.fields.CharField(choices=StatutQuittance.choices, default=StatutQuittance.IMPAYE, max_length=15, null=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    import_stats = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'N°{self.numero} - Montant: {self.solde} FCFA'

    class Meta:
        db_table = 'quittances'
        verbose_name = 'Quittance'
        verbose_name_plural = 'Quittances'

        permissions = [
            ("can_do_annulation_quittance", "Peut annuler des quittances"),
        ]


    @property
    def date_reglement_client(self):
        date_reglement = ''
        if self.solde == 0:
            reglements = self.ses_quittances.filter(Q(statut=StatutValidite.VALIDE))
            last_reglement = reglements.order_by('-id').first()
            date_reglement = last_reglement.date_paiement if last_reglement else ''

        return date_reglement


class TaxeQuittance(models.Model):
    taxe = models.ForeignKey(Taxe, on_delete=models.RESTRICT)
    quittance = models.ForeignKey(Quittance, on_delete=models.RESTRICT)
    montant = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'taxe_quittance'
        verbose_name = 'Autre taxe de la quittance'
        verbose_name_plural = 'Autres taxes de la quittance'


class MouvementQuittance(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    mouvement = models.ForeignKey(Mouvement, on_delete=models.RESTRICT)
    quittance = models.ForeignKey(Quittance, on_delete=models.RESTRICT)
    motif = models.CharField(max_length=255, blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    date_effet = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)

    class Meta:
        db_table = 'mouvement_quittance'
        verbose_name = 'Mouvements sur la quittance'
        verbose_name_plural = 'Mouvements sur les quittances'


def upload_location_operation(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return 'bordereaux/%s.%s' % (file_name, extension)

class Operation(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    nature_operation = models.ForeignKey(NatureOperation, null=True, on_delete=models.CASCADE)
    devise = models.ForeignKey(Devise, null=True, on_delete=models.CASCADE)
    mode_reglement = models.ForeignKey(ModeReglement, null=True, on_delete=models.RESTRICT)
    banque = models.ForeignKey(Banque, null=True, on_delete=models.RESTRICT)
    banque_emettrice = models.CharField(max_length=255, blank=True, null=True)
    compte_tresorerie = models.ForeignKey(CompteTresorerie, null=True, on_delete=models.RESTRICT)
    numero_piece = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True, null=True)
    montant_total = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    nombre_quittances = models.IntegerField(blank=True, null=True)
    fichier = models.FileField(upload_to=upload_location_operation, blank=True, default=None, null=True)
    date_operation = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    observation = models.CharField(max_length=255, null=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    uuid = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'operations'
        verbose_name = "Operation"
        verbose_name_plural = 'Operations'


class Reglement(models.Model):
    bureau = models.ForeignKey(Bureau, null=True, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    reg_deleted_by = models.ForeignKey(User, related_name="reg_deleted_by", null=True, on_delete=models.RESTRICT)
    numero = models.CharField(max_length=50, blank=True, null=True)
    numero_piece = models.CharField(max_length=50, blank=True, null=True)
    mode_reglement = models.ForeignKey(ModeReglement, null=True, on_delete=models.RESTRICT)
    banque = models.ForeignKey(Banque, null=True, on_delete=models.RESTRICT)
    banque_emettrice = models.CharField(max_length=255, blank=True, null=True)
    compte_tresorerie = models.ForeignKey(CompteTresorerie, null=True, on_delete=models.RESTRICT)
    quittance = models.ForeignKey(Quittance, on_delete=models.RESTRICT, related_name="ses_quittances", related_query_name="quittance")
    compagnie = models.ForeignKey(Compagnie, null=True, on_delete=models.RESTRICT, related_name="reglements", related_query_name="reglement")
    devise = models.ForeignKey(Devise, null=True, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    montant_compagnie = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    montant_com_courtage = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    montant_com_gestion = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    montant_com_intermediaire = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    date_paiement = models.DateField(blank=True, null=True)
    observation = models.CharField(max_length=255, null=True)
    motif_annulation = models.CharField(max_length=255, null=True)
    statut_reversement_compagnie = models.fields.CharField(choices=StatutReversementCompagnie.choices, default=StatutReversementCompagnie.NON_REVERSE, max_length=15, null=True)
    statut_commission = models.fields.CharField(choices=StatutEncaissementCommission.choices, default=StatutEncaissementCommission.NON_ENCAISSEE, max_length=15, null=True)
    statut_reglement_apporteurs = models.fields.CharField(choices=StatutReglementApporteurs.choices, default=StatutReglementApporteurs.NON_REGLE, max_length=15, null=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)
    date_reversement_compagnie = models.DateTimeField(null=True)
    date_encaissement_commission = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reglements'
        verbose_name = 'Reglement'
        verbose_name_plural = 'Reglements'

    def montant_com_global(self):
        return self.montant_com_courtage + self.montant_com_gestion
    
    def montant_com_courtage_encaisse(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.GESTION):
            montant += encaissement.montant()
        # print(f"{self.numero} {montant}")
        return montant
    
    def montant_com_courtage_solde(self):
        return (self.montant_com_courtage - self.montant_com_courtage_encaisse())
        
    def montant_com_gestion_encaisse(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.COURTAGE):
            montant += encaissement.montant()
        # print(f"{self.numero} {montant}")
        return montant

    def montant_com_gestion_solde(self):
        return (self.montant_com_gestion - self.montant_com_gestion_encaisse())

    # def montant_com_intermediaire_encaisse(self):
    #     montant = 0
    #     for encaissement in self.encaissement_commissions.all():
    #         montant += encaissement.montant_com_intermediaire
    #     return montant
    #
    # def montant_com_intermediaire_solde(self):
    #     return (self.montant_com_intermediaire - self.montant_com_intermediaire_encaisse())

    def montant_com_encaisse(self):
        return (self.montant_com_courtage_encaisse() + self.montant_com_gestion_encaisse())

    def montant_com_solde(self):
        return (self.montant_com_global() - self.montant_com_encaisse())
    
    def montant_journal_debit(self):
        montant = 0
        for encaissement in self.encaissement_commissions.all():
            for journal in encaissement.journals.all():
                if journal.sens == "D":
                    montant = montant + journal.montant
        return montant 

    def montant_journal_credit(self):
        montant = 0
        for encaissement in self.encaissement_commissions.all():
            for journal in encaissement.journals.all():
                if journal.sens == "C":
                    montant = montant + journal.montant
        return montant

    def montant_journal_debit_courtage(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.GESTION):
            for journal in encaissement.journals.all():
                if journal.sens == "D":
                    montant = montant + journal.montant
        return montant 

    def montant_journal_credit_courtage(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.GESTION):
            for journal in encaissement.journals.all():
                if journal.sens == "C":
                    montant = montant + journal.montant
        return montant
    
    def montant_journal_debit_gestion(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.COURTAGE):
            for journal in encaissement.journals.all():
                if journal.sens == "D":
                    montant = montant + journal.montant
        return montant 

    def montant_journal_credit_gestion(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.COURTAGE):
            for journal in encaissement.journals.all():
                if journal.sens == "C":
                    montant = montant + journal.montant
        return montant
        
    def etat_encaisse_courtage(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.GESTION):
            montant += encaissement.montant()
        #print(montant)
        if montant == self.montant_com_courtage:
            return True
        else:
            return False

    def etat_encaisse_gestion(self):
        montant = 0
        for encaissement in self.encaissement_commissions.exclude(type_commission=TypeEncaissementCommission.COURTAGE):
            montant += encaissement.montant()
        #print(montant)
        if montant == self.montant_com_gestion:
            return True
        else:
            return False

    def etat_encaisse(self):
        if self.etat_encaisse_courtage() == True and self.etat_encaisse_gestion() == True:
            return True
        else:
            return False
        montant = 0
        for encaissement in self.encaissement_commissions.all():
            montant += encaissement.montant()
        #print(montant)
        if montant == self.montant_com_global():
            return True
        else:
            return False
            
    

class OperationReglement(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    operation = models.ForeignKey(Operation, on_delete=models.RESTRICT)
    reglement = models.ForeignKey(Reglement, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut_validite = models.fields.CharField(choices=StatutValidite.choices, default=StatutValidite.VALIDE, max_length=15, null=True)

    class Meta:
        db_table = 'operation_reglement'
        verbose_name = 'Opération sur un règlement'
        verbose_name_plural = 'Opérations sur les règlements'



class Acompte(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, null=True, on_delete=models.RESTRICT)
    quittance = models.ForeignKey(Quittance, null=True, on_delete=models.RESTRICT)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    sens = models.CharField(max_length=1, null=True)
    montant = models.DecimalField(max_digits=20, decimal_places=3, blank=False, null=True)
    date_versement = models.DateField(blank=False, null=True)
    date_affectation = models.DateField(blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'acomptes'
        verbose_name = 'Acompte'
        verbose_name_plural = 'Acomptes'


class TypeDocument(models.Model):
    libelle = models.CharField(max_length=50, blank=True, null=True)
    is_sinistre = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.libelle

    class Meta:
        db_table = 'types_documents'
        verbose_name = 'Type de document'
        verbose_name_plural = "Types de document"


### new code ###

def upload_location_document(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return 'clients/documents/%s.%s' % (file_name, extension)

class Document(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, null=True, on_delete=models.RESTRICT)
    aliment = models.ForeignKey(Aliment, null=True, on_delete=models.RESTRICT)
    type_document = models.ForeignKey(TypeDocument, on_delete=models.RESTRICT)
    quittance = models.ForeignKey(Quittance, null=True, on_delete=models.RESTRICT)
    nom = models.CharField(max_length=255, blank=True, null=True)
    fichier = models.FileField(upload_to=upload_location_document, blank=True, default=None, null=True)
    confidentialite = models.fields.CharField(choices=OptionYesNo.choices, default=OptionYesNo.OUI, max_length=15,null=True)
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'documents'
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


class Filiale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    pays = models.ForeignKey(Pays, blank=True, null=True, on_delete=models.RESTRICT)
    nom = models.CharField(max_length=50, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'filiales'
        verbose_name = 'Filiale'
        verbose_name_plural = 'Filiales'


class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenoms = models.CharField(max_length=50, blank=True, null=True)
    fonction = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nom} {self.prenoms}'

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'



class Vehicule(models.Model):
    categorie_vehicule = models.ForeignKey(CategorieVehicule, on_delete=models.RESTRICT)
    type_carosserie = models.ForeignKey(TypeCarosserie, on_delete=models.RESTRICT)
    marque = models.ForeignKey(MarqueVehicule, on_delete=models.RESTRICT)
    numero_immatriculation = models.CharField(max_length=15, blank=True, null=True)
    numero_immat_provisoire = models.CharField(max_length=15, blank=True, null=True)
    numero_serie = models.CharField(max_length=25, blank=True, null=True)
    modele = models.CharField(max_length=50, blank=True, null=True)
    conducteur = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    energie = models.fields.CharField(choices=Energie.choices, max_length=100, null=True)
    valeur_neuve = models.CharField(max_length=50, blank=True, null=True)
    valeur_actuelle = models.CharField(max_length=50, blank=True, null=True)
    puissance = models.CharField(max_length=50, blank=True, null=True)
    poids_a_vide = models.CharField(max_length=50, blank=True, null=True)
    poids_a_charge = models.CharField(max_length=50, blank=True, null=True)
    date_mis_en_circulation = models.CharField(max_length=50, blank=True, null=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vehicules'
        verbose_name = 'Véhicule'
        verbose_name_plural = 'Véhicules'



class VehiculePolice(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.RESTRICT)
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    formule = models.ForeignKey(FormuleGarantie, null=True, on_delete=models.RESTRICT)
    motif = models.CharField(max_length=255, blank=True, null=True)
    date_mouvement = models.DateTimeField(blank=True, null=True)
    statut = models.fields.CharField(choices=Statut.choices, default=Statut.ACTIF, max_length=15, null=True,
                                     blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vehicule_police'
        verbose_name = 'Véhicule de la police'
        verbose_name_plural = 'Véhicules de la police'



def upload_location_tarifprestataireclient(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return 'clients/tarifs/%s.%s' % (file_name, extension)
class TarifPrestataireClient(models.Model):
    prestataire = models.ForeignKey(Prestataire, on_delete=models.RESTRICT, null=True)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True)
    formule = models.ForeignKey(FormuleGarantie, on_delete=models.RESTRICT, null=True)
    fichier_tarification = models.FileField(upload_to=upload_location_tarifprestataireclient, blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

    class Meta:
        db_table = 'tarif_prestataire_client'
        verbose_name = 'Tarif prestataire-clients'
        verbose_name_plural = 'Tarifs prestataire-clients'

    @property
    def fichier_tarifs(self):
        return mark_safe('<a href="{0}" download>{1}</a>'.format(self.fichier_tarification.url,
                                                                 'Télécharger')) if self.fichier_tarification else ""



## OLEA API MOBILE
class CarteDigitalDematerialisee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    has_digital_card = models.BooleanField(default=False)
    digital_card_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Carte Digitale pour l\'Utilisateur : {self.user.username}'
    
    class Meta:
        db_table = 'cartes_digital_dematerialisees'
        verbose_name = 'Carte Digital Dématérialisée'
        verbose_name_plural = 'Cartes Digital Dématérialisées'




# Les choix pour le champ service
SERVICE_CHOICES = [
    ('production', 'Production'),
    ('sinistre', 'Sinistre'),
    ('comptabilite', 'Comptabilité'),
]

# Les choix pour le champ status
STATUS_CHOICES = [
    ('Actif', 'Actif'),
    ('Inactive', 'Inactive'),
]

class Courrier(models.Model):
    code = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=255)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    # produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sinistre')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.code} - {self.designation} - {self.service} - {self.status} - {self.created_at} "

    class Meta:
        db_table = "production_courrier"