

def check(credit):
    sum_odd = 0
    sum_even = []
    for char in range(len(credit)):
        if char in [1,3,5,7,9,11,13,15,17,19]:
            sum_odd += int(credit[char])
        else:
            sum_even.append(credit[char])

    sum_even = [int(x)*2 for x in sum_even]
    sum_even = [str(x) for x in sum_even]
    sum_even = [int(x[0])+int(x[1]) if len(x) > 1 else int(x) for x in sum_even]
    sum_even = sum(sum_even)
    tot = sum_even + sum_odd
    if tot % 10 == 0:
        print('Credit Card is Valid')
    else:
        print('Credit Card is NOT valid')



credit = '5610591081018250'
false_cred = '1324598354939540'
false_cred2 = '4664232566842988'

check(credit)
