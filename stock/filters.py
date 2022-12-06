from filters import django_filters

class stock(django_filters.FilterSet):
    class Meta:
        model= object
        fields=[
            "モデルフィールド1"
            "モデルフィールド2"
        ]