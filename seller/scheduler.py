from apscheduler.schedulers.background import BackgroundScheduler

from django.apps import apps

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_seller_instances, 'interval', minutes=2)
    scheduler.start()

def check_seller_instances():
    from django.core import management
    management.call_command('check_seller_instances')

start_scheduler()
