def required(data,fields):
    for field in fields:
        if field not in data:
            return False
    return True

def positive_number(value):
    try:
        return float(value)>0
    except:
        return False