from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from Updater import schedule_fct

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_fct.execution, 'interval', weeks=4)
    scheduler.start()