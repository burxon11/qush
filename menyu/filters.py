from django_filters import FilterSet, NumberFilter

from menyu.models import Menyu


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Menyu
        fields = 'category',