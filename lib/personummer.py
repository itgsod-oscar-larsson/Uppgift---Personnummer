__author__ = 'oscar.larsson3'
def valid_pnr(pnr):

    parted = pnr.split('-')

    full = ''.join(parted)

    total = 0

    for n in full[::2]:

        number = int(n)
        multiplied = number * 2

        if multiplied > 9:
            first_digit = int(str(multiplied)[0])
            second_digit = int(str(multiplied)[1])
            total += first_digit + second_digit

        else:
            total += multiplied
    for n in full[1:-1:2]:

        number = int(n)
        total += number

    control_digit = int(full[-1])
    return (total + control_digit) % 10 == 0
