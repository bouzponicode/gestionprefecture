from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
# Create your models here.




class Pays(models.Model):
    c_Pays= models.CharField(max_length=10, null=False)
    paysF = models.CharField(max_length=40, null=False)
    paysA = models.CharField(max_length=40, null=False)
    obsPays = models.CharField(max_length=200, default="RAS")
    def __str__(self):
          return self.paysF

class Region(models.Model):
    c_Region= models.CharField(max_length=10, null=False)
    regionF = models.CharField(max_length=40, null=False)
    regionA = models.CharField(max_length=40, null=False)
    obsRegion = models.CharField(max_length=200, default="RAS")
    pays= models.ForeignKey(Pays, on_delete=models.CASCADE)
    def __str__(self):
          return self.regionF

class Prefecture(models.Model):
    c_Pref= models.CharField(max_length=10, null=False)
    prefF = models.CharField(max_length=40, null=False)
    prefA = models.CharField(max_length=40, null=False)
    obsPref = models.CharField(max_length=200, default="RAS")
    region= models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
          return self.prefF

class Commune(models.Model):
    c_Commune= models.CharField(max_length=10, null=False)
    comF = models.CharField(max_length=40, null=False)
    comA = models.CharField(max_length=40, default="RAS")
    obsComm = models.CharField(max_length=200, null=True)
    pref= models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    def __str__(self):
          return self.comF    

class Quartier(models.Model):
    c_Quartier= models.CharField(max_length=10, null=False)
    quartF = models.CharField(max_length=40, null=False)
    quartA = models.CharField(max_length=40, null=False)
    obsQuart = models.CharField(max_length=200, default="RAS")
    com= models.ForeignKey(Commune, on_delete=models.CASCADE)
    def __str__(self):
          return self.quartF 

class Lotissement(models.Model):
    c_Lotissement= models.CharField(max_length=10, null=False)
    lotF = models.CharField(max_length=40, null=False)
    lotA = models.CharField(max_length=40, null=False)
    obsLot = models.CharField(max_length=200, default="RAS")
    quartier= models.ForeignKey(Quartier, on_delete=models.CASCADE)
    def __str__(self):
          return self.lotF

class Residence(models.Model):
    c_Residence= models.CharField(max_length=10, null=False)
    resF = models.CharField(max_length=40, null=False)
    resA = models.CharField(max_length=40, null=False)
    obsRes = models.CharField(max_length=200, default="RAS")
    quartier= models.ForeignKey(Quartier, on_delete=models.CASCADE)
    def __str__(self):
          return self.lotF

class Boulevard(models.Model):
    bdF = models.CharField(max_length=80, null=True)
    bdA = models.CharField(max_length=80, null=True)
    obsBd = models.CharField(max_length=200, default="RAS")
    quart= models.ForeignKey(Quartier, on_delete=models.CASCADE)
    def __str__(self):
          return self.bdF 

class Rue(models.Model):
    rueF = models.CharField(max_length=80, null=True)
    rueA = models.CharField(max_length=80, null=True)
    obsrue = models.CharField(max_length=200, default="RAS")
    quart= models.ForeignKey(Quartier, on_delete=models.CASCADE)
    def __str__(self):
          return self.rueF 
           
class Autre(models.Model):
    autreF = models.CharField(max_length=80, null=True)
    autreA = models.CharField(max_length=80, null=True)
    obsAutre = models.CharField(max_length=200, default="RAS")
    quart= models.ForeignKey(Quartier, on_delete=models.CASCADE)
    def __str__(self):
          return self.autreF 

class Adresse(models.Model):
    prefecture= models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    commune= models.ForeignKey(Commune, on_delete=models.CASCADE)
    quartier= models.ForeignKey(Quartier, on_delete=models.CASCADE)

class Grade(models.Model):
    c_Grade= models.CharField(max_length=10, null=False)
    gradF = models.CharField(max_length=40, null=False)
    gradA = models.CharField(max_length=40, null=False)
    obsGrad = models.CharField(max_length=200, default="RAS")
    def __str__(self):
          return self.gradF    

class Person(models.Model):
    #user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    SEXE = {('M','Masculin'),('F','Feminin')}
    nom = models.CharField(max_length=190, null=True)
    prenom = models.CharField(max_length=190, null=True)
    d_naissance= models.DateField()
    l_naissance = models.CharField(max_length=20,default="Mohammedia")
    d_created = models.DateField(auto_now_add=True, null=True)
    d_Modified = models.DateField(auto_now_add=True, null=True)
    active_Person = models.BooleanField(null=False)
    obsPerson = models.CharField(max_length=4,default="RAS")
    sexe = models.CharField(max_length=1,null=False,choices=SEXE)
    #adresse= models.ForeignKey(Adresse, on_delete=models.CASCADE)
    def __str__(self):
        return (self.nom)
    



class Enf(Person):
    cin_Parent = models.CharField(max_length=8, null=True)
class Conjoint(Person):
    cin = models.CharField(max_length=8, null=True)
    cin_Conjoint = models.CharField(max_length=8, null=True)
class Taux_Anc(models.Model):
    code_taux_anc= models.CharField(max_length=5, null=True)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    taux_Anc = models.CharField(max_length=190, null=True)
    m_Anc = models.DecimalField(max_digits=5,decimal_places=2)
    obsTA = models.CharField(max_length=200, default="RAS")
    def __str__(self):
        return str(self.code_taux_anc)
class Type(models.Model):
    c_type= models.CharField(max_length=10)
    l_type= models.CharField(max_length=100)
    obsType= models.CharField(max_length=200, default="RAS",null=True)
    def __str__(self):
        return str(self.c_type)
class Periode(models.Model):
    #code_Periode = models.CharField(max_length=4)
    d_Effet = models.DateField()
    d_fin_eng = models.DateField()
    d_deb_rap = models.DateField()
    d_fin_rap = models.DateField()
    type= models.ForeignKey(Type,on_delete= models.CASCADE)
    objet = models.CharField(max_length=255, null=False)
    active_Periode = models.BooleanField()
    obsPerio = models.CharField(max_length=200, default="RAS")
    def __str__(self):
        return str(self.d_Effet)
class Interval(models.Model):
    d_debut = models.DateField()
    d_fin = models.DateField()
    obsIntrval = models.CharField(max_length=200, default="RAS")
    def __str__(self):
        return str(self.d_debut)
class Situation(models.Model):
    c_Situation = models.CharField(max_length=6)
    grade = models.ForeignKey(Grade,on_delete= models.CASCADE)
    code_taux_anc = models.ForeignKey(Taux_Anc,on_delete= models.CASCADE)
    nbre_enf = models.PositiveSmallIntegerField(max_length=1)
    obsSit = models.CharField(max_length=200, default="RAS")
    def __str__(self):
        return str(self.c_Situation)

class SitFin(models.Model):
    sit= models.ForeignKey(Situation,on_delete=models.CASCADE)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    periode = models.ForeignKey(Periode,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.sit} {self.type} {self.periode}'
    
class Ref(Person):
        cin = models.CharField(max_length=8, null=True)
        mle = models.IntegerField(blank=True, null=True, default=1200)
        email = models.EmailField(blank=True, null=True, default="preson.png")
        phone = models.CharField(max_length=190, null=True)
        photo = models.ImageField(blank=True, null=True, default="preson.png")
        d_recrut = models.DateField(null=True)
        sitFin= models.ForeignKey(SitFin,on_delete=models.CASCADE)
        

class Tb(models.Model):# Traitement de base
    grade= models.ForeignKey(Grade,on_delete= models.CASCADE)
    mont_Tb = models.DecimalField(max_digits=7, decimal_places=2)
    obsTb = models.CharField(max_length=200, default="RAS")
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)

class Ir(models.Model):# Indémnité de representation
    grade= models.ForeignKey(Grade,on_delete= models.CASCADE)
    mont_Ir = models.DecimalField(max_digits=7, decimal_places=2)
    obsIr = models.CharField(max_length=200, default="RAS")
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)

class It(models.Model):# Indemnité de tournée
    grade= models.ForeignKey(Grade,on_delete= models.CASCADE)
    mont_It = models.DecimalField(max_digits=7, decimal_places=2)
    obsIt = models.CharField(max_length=200, default="RAS")
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)

class If(models.Model):# Indemnité de fonction
    grade= models.ForeignKey(Grade,on_delete= models.CASCADE)
    mont_If = models.DecimalField(max_digits=7, decimal_places=2)
    obsIf = models.CharField(max_length=200, default="RAS")
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)

class Af(models.Model):# Allocations familiales
    mont_If = models.DecimalField(max_digits=7, decimal_places=2)
    obsIf = models.CharField(max_length=200, null=True)
    code_Periode= models.ForeignKey(Interval, on_delete=models.CASCADE)

class Rcar(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_Rcar = models.DecimalField(max_digits=3,decimal_places=2)

class Amo(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_Amo = models.DecimalField(max_digits=3,decimal_places=2)

class Sm(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_Sm = models.DecimalField(max_digits=3,decimal_places=2)

class Caad(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_Caad = models.DecimalField(max_digits=3,decimal_places=2)   

class Igr(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_Igr = models.DecimalField(max_digits=3,decimal_places=2) 

class NetM(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_NetM = models.DecimalField(max_digits=3,decimal_places=2)

class BruteM(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    code_Interval= models.ForeignKey(Interval, on_delete=models.CASCADE)
    montant_BruteM = models.DecimalField(max_digits=3,decimal_places=2) 


class Solde(models.Model):
    c_Situation = models.ForeignKey(Situation,on_delete=models.CASCADE)
    #code_Periode= models.ForeignKey(Periode, on_delete=models.CASCADE)
    tba = models.DecimalField(max_digits=6,decimal_places=2)
    anca = models.DecimalField(max_digits=6,decimal_places=2)
    ifa = models.DecimalField(max_digits=6,decimal_places=2)
    ira = models.DecimalField(max_digits=6,decimal_places=2)
    ita = models.DecimalField(max_digits=6,decimal_places=2)
    afa = models.DecimalField(max_digits=6,decimal_places=2)
    ba = models.DecimalField(max_digits=6,decimal_places=2)
    bm = models.DecimalField(max_digits=6,decimal_places=2)
    rcar = models.DecimalField(max_digits=6,decimal_places=2)
    amo = models.DecimalField(max_digits=6,decimal_places=2)
    sm = models.DecimalField(max_digits=6,decimal_places=2)
    caad = models.DecimalField(max_digits=6,decimal_places=2)
    igr = models.DecimalField(max_digits=6,decimal_places=2)
    netm = models.DecimalField(max_digits=6,decimal_places=2)
    rcarp = models.DecimalField(max_digits=6,decimal_places=2)
    cnops = models.DecimalField(max_digits=6,decimal_places=2)
    obsSit = models.CharField(max_length=200, default="RAS")