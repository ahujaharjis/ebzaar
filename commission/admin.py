from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DefaultRate)
admin.site.register(Penalty)
admin.site.register(ConcessionalRate)
admin.site.register(Reimbursement)
admin.site.register(DeliveryZone)
admin.site.register(Penalty_orders)
admin.site.register(Promo)
admin.site.register(AdditionalCommRate)
admin.site.register(PgFile)