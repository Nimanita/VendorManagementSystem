from django.dispatch import Signal

# create a signal instance for order confirmation
order_created = Signal()
order_update = Signal()