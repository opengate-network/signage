# flake8: noqa: E501


def weather_code_to_info(weather_code: int) -> tuple:
    match weather_code:
        case 0:
            return tuple(['sunny', 'Soleil'])
        case 1:
            return tuple(['partlysunny', 'Peu nuageux'])
        case 2:
            return tuple(['partially-cloudy', 'Ciel voilé'])
        case 3:
            return tuple(['mostly-cloudy', 'Nuageux'])
        case 4:
            return tuple(['mostly-cloudy', 'Très nuageux'])
        case 5:
            return tuple(['cloudy', 'Couvert'])
        case 6:
            return tuple(['fog', 'Brouillard'])
        case 7:
            return tuple(['fog', 'Brouillard givrant'])
        case 10:
            return tuple(['rain', 'Pluie faible'])
        case 11:
            return tuple(['rain', 'Pluie modérée'])
        case 12:
            return tuple(['rain', 'Pluie forte'])
        case 13:
            return tuple(['rain', 'Pluie faible verglaçante'])
        case 14:
            return tuple(['rain', 'Pluie modérée verglaçante'])
        case 15:
            return tuple(['rain', 'Pluie verglaçante'])
        case 16:
            return tuple(['drizzle', 'Bruine'])
        case 20:
            return tuple(['snow', 'Neige faible'])
        case 21:
            return tuple(['snow', 'Neige modérée'])
        case 22:
            return tuple(['snow', 'Neige forte'])
        case 30:
            return tuple(['sleet', 'Pluie et neige mêlées faibles'])
        case 31:
            return tuple(['sleet', 'Pluie et neige mêlées modérées'])
        case 32:
            return tuple(['sleet', 'Pluie et neige mêlées fortes'])
        case 40:
            return tuple(['rain', 'Averses de pluie locales et faibles'])
        case 41:
            return tuple(['rain', 'Averses de pluie locales'])
        case 42:
            return tuple(['rain', 'Averses locales et fortes'])
        case 43:
            return tuple(['rain', 'Averses de pluie faibles'])
        case 44:
            return tuple(['rain', 'Averses de pluie'])
        case 45:
            return tuple(['rain', 'Averses de pluie fortes'])
        case 46:
            return tuple(['rain', 'Averses de pluie faibles et fréquentes'])
        case 47:
            return tuple(['rain', 'Averses de pluie fréquentes'])
        case 48:
            return tuple(['rain', 'Averses de pluie fortes et fréquentes'])
        case 60:
            return tuple(['snow', 'Averses de neige localisées et faibles'])
        case 61:
            return tuple(['snow', 'Averses de neige localisées'])
        case 62:
            return tuple(['snow', 'Averses de neige localisées et fortes'])
        case 63:
            return tuple(['snow', 'Averses de neige faibles'])
        case 64:
            return tuple(['snow', 'Averses de neige'])
        case 65:
            return tuple(['snow', 'Averses de neige fortes'])
        case 66:
            return tuple(['snow', 'Averses de neige faibles et fréquentes'])
        case 67:
            return tuple(['snow', 'Averses de neige fréquentes'])
        case 68:
            return tuple(['snow', 'Averses de neige fortes et fréquentes'])
        case 70:
            return tuple(['sleet', 'Averses de pluie et neige mêlées localisées et faibles'])
        case 71:
            return tuple(['sleet', 'Averses de pluie et neige mêlées localisées'])
        case 72:
            return tuple(['sleet', 'Averses de pluie et neige mêlées localisées et fortes'])
        case 73:
            return tuple(['sleet', 'Averses de pluie et neige mêlées faibles'])
        case 74:
            return tuple(['sleet', 'Averses de pluie et neige mêlées'])
        case 75:
            return tuple(['sleet', 'Averses de pluie et neige mêlées fortes'])
        case 76:
            return tuple(['sleet', 'Averses de pluie et neige mêlées faibles et nombreuses'])
        case 77:
            return tuple(['sleet', 'Averses de pluie et neige mêlées fréquentes'])
        case 78:
            return tuple(['sleet', 'Averses de pluie et neige mêlées fortes et fréquentes'])
        case 100:
            return tuple(['thunderstorm', 'Orages faibles et locaux'])
        case 101:
            return tuple(['thunderstorm', 'Orages locaux'])
        case 102:
            return tuple(['thunderstorm', 'Orages fort et locaux'])
        case 103:
            return tuple(['thunderstorm', 'Orages faibles'])
        case 104:
            return tuple(['thunderstorm', 'Orages'])
        case 105:
            return tuple(['thunderstorm', 'Orages forts'])
        case 106:
            return tuple(['thunderstorm', 'Orages faibles et fréquents'])
        case 107:
            return tuple(['thunderstorm', 'Orages fréquents'])
        case 108:
            return tuple(['thunderstorm', 'Orages forts et fréquents'])
        case 120:
            return tuple(['thunderstorm', 'Orages faibles et locaux de neige ou grésil'])
        case 121:
            return tuple(['thunderstorm', 'Orages locaux de neige ou grésil'])
        case 122:
            return tuple(['thunderstorm', 'Orages locaux de neige ou grésil'])
        case 123:
            return tuple(['thunderstorm', 'Orages faibles de neige ou grésil'])
        case 124:
            return tuple(['thunderstorm', 'Orages de neige ou grésil'])
        case 125:
            return tuple(['thunderstorm', 'Orages de neige ou grésil'])
        case 126:
            return tuple(['thunderstorm', 'Orages faibles et fréquents de neige ou grésil'])
        case 127:
            return tuple(['thunderstorm', 'Orages fréquents de neige ou grésil'])
        case 128:
            return tuple(['thunderstorm', 'Orages fréquents de neige ou grésil'])
        case 130:
            return tuple(['thunderstorm', 'Orages faibles et locaux de pluie et neige mêlées ou grésil'])
        case 131:
            return tuple(['thunderstorm', 'Orages locaux de pluie et neige mêlées ou grésil'])
        case 132:
            return tuple(['thunderstorm', 'Orages fort et locaux de pluie et neige mêlées ou grésil'])
        case 133:
            return tuple(['thunderstorm', 'Orages faibles de pluie et neige mêlées ou grésil'])
        case 134:
            return tuple(['thunderstorm', 'Orages de pluie et neige mêlées ou grésil'])
        case 135:
            return tuple(['thunderstorm', 'Orages forts de pluie et neige mêlées ou grésil'])
        case 136:
            return tuple(['thunderstorm', 'Orages faibles et fréquents de pluie et neige mêlées ou grésil'])
        case 137:
            return tuple(['thunderstorm', 'Orages fréquents de pluie et neige mêlées ou grésil'])
        case 138:
            return tuple(['thunderstorm', 'Orages forts et fréquents de pluie et neige mêlées ou grésil'])
        case 140:
            return tuple(['thunderstorm', 'Pluies orageuses'])
        case 141:
            return tuple(['thunderstorm', 'Pluie et neige mêlées à caractère orageux'])
        case 142:
            return tuple(['thunderstorm', 'Neige à caractère orageux'])
        case 210:
            return tuple(['rain', 'Pluie faible intermittente'])
        case 211:
            return tuple(['rain', 'Pluie modérée intermittente'])
        case 212:
            return tuple(['rain', 'Pluie fortes intermittente'])
        case 220:
            return tuple(['snow', 'Neige faible intermittente'])
        case 221:
            return tuple(['snow', 'Neige modérée intermittente'])
        case 212:
            return tuple(['snow', 'Neige forte intermittente'])
        case 230:
            return tuple(['drizzle', 'Pluie et neige mêlées'])
        case 231:
            return tuple(['drizzle', 'Pluie et neige mêlées'])
        case 232:
            return tuple(['drizzle', 'Pluie et neige mêlées'])
        case 235:
            return tuple(['drizzle', 'Averses de grêle'])
        