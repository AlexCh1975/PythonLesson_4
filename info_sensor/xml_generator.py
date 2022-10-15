from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(devace = 1):
    xml = '<xml>\n'
    xml += '    <temperature units = "C">{}</temperature>\n'\
        .format(temperature_view(devace))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(devace))
    xml += '    <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(wind_speed_view(devace))
    xml += '</xml>'

    with open('data.xml', 'w', encoding='utf-8') as page:
        page.write(xml)

    return xml


def new_create(data, devace = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '    <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(w)
    xml += '</xml>'

    with open('new_data.xml', 'w', encoding='utf-8') as page:
        page.write(xml)

    return data