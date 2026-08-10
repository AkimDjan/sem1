
def int_to_roman(int_number: int) -> str:
    convertions=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

    result=''
    for num, r_num in convertions:
        while int_number>=num:
            result+=r_num
            int_number-=num
    return result

print(int_to_roman(int(input())))




    
    