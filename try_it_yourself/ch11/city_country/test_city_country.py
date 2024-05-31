from city_country import city_country


def test_city_country():
    formatted_city_country = city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'
