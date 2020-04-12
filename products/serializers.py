from django.db.models import Sum
from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    stock_card = serializers.SerializerMethodField()

    def get_username(self, obj):
        if obj.user:
            return obj.user.username
        return '-'

    def get_stock_card(self, obj):
        if not obj.is_init:
            stock_cards = obj.productstockcard.all()
            queryset = stock_cards.aggregate(
                total_in=Sum('total_in'),
                total_out=Sum('total_out'),
                end_balance=Sum('total_in') - Sum('total_out')
            )

            return {
                'init_balance': '{} {} '.format(queryset.get('init_balance'), obj.unit),
                'total_in': '{} {}'.format(queryset.get('total_in'), obj.unit),
                'total_out': '{} {}'.format(queryset.get('total_out'), obj.unit),
                'end_balance': '{} {}'.format(queryset.get('end_balance'), obj.unit)
            }
        return {
            'init_balance': '0 {}'.format(obj.unit),
            'total_in': '0 {}'.format(obj.unit),
            'total_out': '0 {}'.format(obj.unit),
            'end_balance': '0 {}'.format(obj.unit)
        }

    class Meta:
        model = Product
        fields = '__all__'
