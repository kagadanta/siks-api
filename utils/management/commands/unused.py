from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.datetime_safe import datetime

from products.models import Product
from stocks.models import StockIn, StockOut
from users.models import Supplier, Customer


class Command(BaseCommand):
    help = 'Utilitas data tidak terpakai'
    objects = [
        'customer',
        'supplier',
        'product',
        'stockin',
        'stockout',
        'all',
    ]
    actions = [
        'show',
        'clear'
    ]

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help='Menghapus objek data yang tidak terpakai')
        parser.add_argument('-r', '--resource', type=str, nargs='+', help='Sumber objek data yang ingin dihapus/ditampilkan')

    def action_show(self):
        how_many_days = 0
        days = timedelta(days=how_many_days)

        unused_data_supplier = Supplier.objects.filter(
            is_init=True
        ).count()

        unused_data_customer = Customer.objects.filter(
            is_init=True
        ).count()

        unused_data_product = Product.objects.filter(
            is_init=True
        ).count()

        unused_data_stock_in = StockIn.objects.filter(
            is_init=True
        ).count()

        unused_data_stock_out = StockOut.objects.filter(
            is_init=True
        ).count()

        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Unused Supplier\t:\t "(%i) Data"' % (unused_data_supplier,)))
        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Unused Customer\t:\t "(%i) Data"' % (unused_data_customer,)))
        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Unused Product\t:\t "(%i) Data"' % (unused_data_product,)))
        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Unused Stock\t:\t "(%i) Stock In, (%i) Stock Out"' % (
            unused_data_stock_in,
            unused_data_stock_out
        )))

    def action_clear(self, objects):
        for i in objects:
            if i == 'customer' or i == 'all':
                Customer.objects.filter(is_init=True).delete()
                self.stdout.write(
                    self.style.SUCCESS('Unused customer data was successfully removed')
                )

            if i == 'supplier' or i == 'all':
                Supplier.objects.filter(is_init=True).delete()
                self.stdout.write(
                    self.style.SUCCESS('Unused supplier data was successfully removed')
                )

            if i == 'product' or i == 'all':
                Product.objects.filter(is_init=True).delete()
                self.stdout.write(
                    self.style.SUCCESS('Unused product data was successfully removed')
                )

            if i == 'stockin' or i == 'all':
                StockIn.objects.filter(is_init=True).delete()
                self.stdout.write(
                    self.style.SUCCESS('Unused stock in data was successfully removed')
                )

            if i == 'stockout' or i == 'all':
                StockOut.objects.filter(is_init=True).delete()
                self.stdout.write(
                    self.style.SUCCESS('Unused stock out data was successfully removed')
                )


    def handle(self, *args, **kwargs):
        action = kwargs.get('action')
        resource = kwargs.get('resource') if kwargs.get('resource') else ['all']
        self.action_show()

        if action in self.actions:
            if action == 'show':
                self.action_show()
            if action == 'clear':
                if bool(len({*resource} & {*self.objects})):
                    self.action_clear(resource)