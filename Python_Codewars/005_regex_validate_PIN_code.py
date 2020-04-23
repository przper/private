def validate_pin(pin):
    if len(str(pin))==4 or len(str(pin))==6:
        if str(pin).isdigit():
            return True
        else:
            return False
    else:
        return False

pin = '-1.234'
print(validate_pin(pin))
