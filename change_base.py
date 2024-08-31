def base(text, text_base, output_base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    if not (2 <= text_base <= 36) and (2 <= output_base <= 36):
        print('Base must be between 2 and 36')

    dec = int(text, text_base)

    while dec > 0:
        rem = dec % output_base
        res = digits[rem] + res
        dec //= output_base

    return res
print(base("100",2,4))
