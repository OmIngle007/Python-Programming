def subtract_binary(bin1, bin2):

    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    result = ''
    borrow = 0


    for i in range(max_len - 1, -1, -1):
        b1 = int(bin1[i])
        b2 = int(bin2[i])


        if borrow == 1:
            if b1 == 0:
                b1 = 1
                borrow = 1
            else:
                b1 = 0
                borrow = 0

        if b1 < b2:
            borrow = 1


        result = str(b1 - b2) + result


    result = result.lstrip('0')


    return result if result else '0'


bin1 = "1011"  
bin2 = "1001"  

result = subtract_binary(bin1, bin2)
print(f"Subtraction result of {bin1} - {bin2} in binary: {result}")

