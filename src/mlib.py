def fmt_name(fname, lname):
    return f'{fname.strip().capitalize()} {lname.strip().upper()}'


def gen_email(fname, lname, domain):
    return f'{fname.strip().lower()}.{lname[0].strip().lower()}@{domain.strip()}'


def price_vat(amt, vat_rate=.07):
    vat = round(amt * vat_rate / (1 + vat_rate), 2)
    price = round(amt - vat, 2)
    return (price, vat)


if __name__ == "__main__":
    print(price_vat(120, .1))
    print(gen_email('Peter', 'Parker', 'marvel.com'))
