import re


def find_city(city):
    regex_num = re.compile('[a-zA-Z]+')
    s = regex_num.search(city)
    try:
        return city[s.start():s.end()]
    except AttributeError:
        return ""

