def get_zodiac_sign(date_string):
    """ Parses birth date assuming the incoming date string is in YYYY-mm-dd
    format. No datetime module or other imports are required.
    Zodiac calendar date ranges were taken from https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BA%D0%B8_%D0%B7%D0%BE%D0%B4%D0%B8%D0%B0%D0%BA%D0%B0#%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5_%D0%B2_%D0%B7%D0%BD%D0%B0%D0%BA%D0%B0%D1%85_%D0%B7%D0%BE%D0%B4%D0%B8%D0%B0%D0%BA%D0%B0, those may vary depending on tradition. """
    zodiac = {
        "01": {
            "threshold": 19,
            "before": "Козерог",
	    "after": "Водолей"
	},
	"02": {
            "threshold": 18,
	    "before": "Водолей",
	    "after": "Рыбы"
	},
	"03": {
            "threshold": 20,
	    "before": "Рыбы",
	    "after": "Овен"
	},
	"04": {
            "threshold": 19,
	    "before": "Овен",
	    "after": "Телец"
	},
	"05": {
            "threshold": 20,
	    "before": "Телец",
	    "after": "Близнецы"
	},
	"06": {
            "threshold": 20,
	    "before": "Близнецы",
	    "after": "Рак"
	},
	"07": {
            "threshold": 22,
	    "before": "Рак",
	    "after": "Лев"
	},
	"08": {
            "threshold": 22,
	    "before": "Лев",
	    "after": "Дева"
	},
	"09": {
            "threshold": 22,
	    "before": "Дева",
	    "after": "Весы"
	},
	"10": {
            "threshold": 22,
	    "before": "Весы",
	    "after": "Скорпион"
	},
	"11": {
            "threshold": 21,
	    "before": "Скорпион",
	    "after": "Стрелец"
	},
	"12": {
            "threshold": 21,
	    "before": "Стрелец",
	    "after": "Козерог"
	},
    }
	
    date_parts = date.split("-")
    month = date_parts[1]
    day = int(date_parts[2])
    
    if day <= zodiac[month]["threshold"]:
	return zodiac[month]["before"]
    else:
        return zodiac[month]["after"]
