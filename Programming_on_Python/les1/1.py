def roman_to_int(roman_number: str) -> int:
    convertions={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result=0

    for i in range(0,len(roman_number)-1):
        if convertions[roman_number[i]]<convertions[roman_number[i+1]]:
            result-=convertions.setdefault(roman_number[i])
        else:
            result+=convertions.setdefault(roman_number[i])
    result+=convertions.setdefault(roman_number[-1])
    return result

print(roman_to_int(input()))