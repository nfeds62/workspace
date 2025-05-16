def ticket_price(age):
    if age < 13:
        return "You are to young to for the ride."
    elif age == 13 or age < 18:
        return "Your ticket price is $8.00."
    else:
        return "Your ticket price is $12.00."
