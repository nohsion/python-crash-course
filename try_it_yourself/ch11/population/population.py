def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    return f"{city.title()}, {country.title()} - population {population}"


def city_country_optional(city, country, population=0):
    """Return a string like 'Santiago, Chile' or 'Santiago, Chile'."""
    default_output = f"{city.title()}, {country.title()}"
    if population:
        default_output += f" - population {population}"
    return default_output
