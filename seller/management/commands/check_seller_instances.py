# import time
# from django.core.management.base import BaseCommand
# from django.utils import timezone
# from seller.models import Seller

# class Command(BaseCommand):
#     help = 'Check and delete Seller instances with is_seller=False created 2 minutes ago'

#     def handle(self, *args, **kwargs):
#         two_minutes_ago = timezone.now() - timezone.timedelta(minutes=2)
#         sellers_to_delete = Seller.objects.filter(is_seller=False, created__lte=two_minutes_ago)

#         for seller in sellers_to_delete:
#             seller.delete()

#         self.stdout.write(self.style.SUCCESS('Successfully checked and deleted Seller instances.'))
