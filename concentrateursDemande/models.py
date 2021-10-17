from django.conf import settings
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
import datetime
from datetime import date
import django.utils
from django.utils import timezone, dateformat

class Demande(models.Model):
    COMMUNE_CHOICES=(('1', 'باب الواد'), ('2', 'برج البحري'), ('3', 'أولاد شبل'), ('4', 'أولاد فايت'), ('5', 'الأبيار'), ('6', 'الجزائر الوسطى'), ('7', 'الحامة - العناصر'), ('8', 'الحراش'), ('9', 'الحمامات'), ('10', 'الدار البيضاء'), ('11', 'الرايس حميدو'), ('12', 'الرحمانية'), ('13', 'الرغاية'), ('14', 'الرويبة'), ('15', 'السحاولة'), ('16', 'السويدانية'), ('17', 'الشراقة'), ('18', 'العاشور'), ('19', 'القبة'), ('20', 'القصبة'), ('21', 'الكاليتوس'), ('22', 'المحالمة'), ('23', 'المحمدية'), ('24', 'المدنية'), ('25', 'المرادية'), ('26', 'المرسى'), ('27', 'المقارية'), ('28', 'بئر توتة'), ('29', 'بئر خادم'), ('30', 'بئر مراد رايس'), ('31', 'باب الزوار'), ('32', 'باب الواد'), ('33', 'بابا حسن'), ('34', 'باش جراح'), ('35', 'براقي'), ('36', 'برج البحري'), ('37', 'برج الكيفان'), ('38', 'بن عكنون'), ('39', 'بني مسوس'), ('40', 'بوروبة'), ('41', 'بوزريعة'), ('42', 'بولوغين'), ('43', 'جسر قسنطينة'), ('44', 'حسين داي'), ('45', 'حيدرة'), ('46', 'خرايسية'), ('47', 'دالي إبراهيم'), ('48', 'دويرة'), ('49', 'زرالدة'), ('50', 'سطاوالي'), ('51', 'سيدي موسى'), ('52', 'عين البنيان'), ('53', 'عين طاية'), ('54', 'هراوة'), ('55', 'واد قريش'), ('56', 'وادي السمار'), ('57', 'بوزريعة'), ('58', 'تسالة المرجة'))
    ORDO_CHOICES=(('1', 'نعم, مرض كوفيد'),('2', 'نعم, مرض رئوي اخر'),('3', 'لا'))
    MALADIE_CHOICES=(('1', 'لا'),('2', 'السكري'),('3', 'ارتفاع ضغط الدم'),('4', 'مرض رئوي مزمن'),('5', 'السرطان'),('6', 'متلازمة داون'),('7', 'مرض القلب'),('8', 'حامل'),('9', 'الربو'),('10', 'إعاقة'),('11', 'مرض مزمن اخر, يذكر في الملاحظة'))
    ENDROIT_CHOICES=(('1', 'المنزل'),('2', 'المستشفى'))
    OXY_CHOICES=(('1', '10-20'),('2', '20-30'),('3', '30-40'),('4', '40-50'),('5', '50-60'),('6', '60-70'),('7', '70-80'),('8', '80-90'),('9', '90-100'))
    TRAITE_CHOICES=(('1', 'لا'),('2', 'نعم'))

    NCI = models.CharField(verbose_name='رقم بطاقة التعريف الوطنية',default='', unique=True,max_length=200)
    nomPrenom = models.CharField(verbose_name='الإسم و اللقب',default='',max_length=200)
    Age = models.IntegerField(verbose_name='العمر',default=0)
    numeroTel = PhoneNumberField(verbose_name='رقم هاتف مرافق المريض',default='+213', region="AG")
    commune = models.CharField(verbose_name='البلدية',default='1',max_length=200,choices=COMMUNE_CHOICES)
    adresse = models.CharField(verbose_name='العنوان',default='',max_length=200)
    poids = models. FloatField(verbose_name='الوزن',default=0.0)
    oxygene = models.CharField(verbose_name='نسبة الأكسجين في الدم',max_length=200,choices=OXY_CHOICES,default='8')
    ordonnance = models.CharField(verbose_name='هل لديك وصفة ؟',max_length=200,choices=ORDO_CHOICES,default='1')
    medecin = models.CharField(verbose_name='إسم الطبيب المعالج',max_length=200,default='', blank=True)
    NumMedecin = PhoneNumberField(verbose_name='رقم الطبيب المعالج',default='+213', region="AG", blank=True)
    endroit = models.CharField(verbose_name='مكان تواجد المريض',max_length=200,choices=ENDROIT_CHOICES,default='1')
    maladieChronique = models.CharField(verbose_name='هل لدى المريض أمراض مزمنة ؟',max_length=200,choices=MALADIE_CHOICES,default='1')
    autre = models.TextField(verbose_name='ملاحظات أخرى',blank=True)
    traite = models.CharField(verbose_name='تم معالجة الطلب',choices=TRAITE_CHOICES,default='1',max_length=10, blank=True)
    dateDemande = models.DateField(verbose_name='تاريخ تسليم المكثف', default=dateformat.format(timezone.now(), 'Y-m-d'))

    def __str__(self):
        return self.NCI


class Concentrateur(models.Model):
    DISPO_CHOICES=(('1', 'لا'),('2', 'نعم'))

    Reference = models.CharField(verbose_name='الرقم التسلسلي',default='', unique=True,max_length=200)
    Debit = models.FloatField(verbose_name='الحد الأقصى للتدفق LMP',default=0.0)
    pression = models.FloatField(verbose_name='ضغط المخرج PSI',default=0.0)
    electrique = models.FloatField(verbose_name='الكهرباء HZ',default=0.0,blank=True)
    concentration = models.CharField(verbose_name='تركيز الأكسجين',default='',max_length=200)
    sonore =  models.FloatField(verbose_name='مستوى الصوت DB',default=0.0,blank=True)
    dimensions = models.CharField(verbose_name='الأبعاد HxLxP',default='',max_length=200,blank=True)
    poids = models.FloatField(verbose_name='الوزن KG',default=0.0,blank=True)
    soupage = models.CharField(verbose_name='صمام الإغاثة',default='',max_length=200,blank=True)    
    autre = models.TextField(verbose_name='ملاحظات أخرى',blank=True)
    disponible = models.CharField(verbose_name='متوفر',choices=DISPO_CHOICES,default='2',max_length=10, blank=True)

    def __str__(self):
        return self.Reference


class DemandeTraite(models.Model):
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE,verbose_name='رقم بطاقة التعريف الوطنية', limit_choices_to={'traite':'1'})
    concentrateur = models.ForeignKey(Concentrateur, on_delete=models.CASCADE,verbose_name='الرقم التسلسلي', limit_choices_to={'disponible':'2'})
    date = models.DateField(verbose_name='تاريخ تسليم المكثف', default=dateformat.format(timezone.now(), 'Y-m-d'))
    dateRetour = models.DateField(verbose_name='تاريخ إعادة المكثف', blank=True, null=True)

    def __str__(self):
        return self.demande.NCI