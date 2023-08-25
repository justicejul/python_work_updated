# def city_country_name(city, country):
#     info = f"{city}, {country}"
#     return info


# def city_country_name(city, country, population):
#     info = f"{city}, {country} - population {population}"
#     return info


def city_country_name(city, country, population=""):
    if population:
        info = f"{city}, {country} - population {population}"
        return info
    else:
        info = f"{city}, {country}"
        return info

kaduna = city_country_name("Barnawa", "Kaduna")
print(kaduna)
