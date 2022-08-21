import re
plate_regex = "^[a-zA-Z]{1,3}-[a-zA-Z]{1,2}[1-9][0-9]{0,3}$"


def validate_plate(input):
    try:
        data = input.get('plate', None)

        if data is None:
            return None
        if re.match(plate_regex, data):
            return True
        else:
            return False
    except:
        return None
