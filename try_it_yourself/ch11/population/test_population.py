from population import city_country, city_country_optional

def test_city_country():
    formatted_city_country = city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile - population'

    formatted_city_country = city_country('santiago', 'chile', 5000000)
    assert formatted_city_country == 'Santiago, Chile - population 5000000'


def test_city_country_optional():
    formatted_city_country = city_country_optional('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'

    formatted_city_country = city_country_optional('santiago', 'chile', 5000000)
    assert formatted_city_country == 'Santiago, Chile - population 5000000'

