import time
import os
from concentrateursDemande.models import  Demande
import datetime 
from datetime import datetime
from dateutil.relativedelta import relativedelta

def execution():  
	startDate = datetime.strftime(datetime.today()- relativedelta(months=1), '%Y-%m-%d')
	print(startDate)
	Demande.objects.filter(dateDemande__lte = startDate).filter(traite=1).delete()