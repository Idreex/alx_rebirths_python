#!/usr/bin/python3

def roman_to_int(roman_string):
    table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev, sum = 0, 0

    for c in roman_string:
        sum += table[c] if table[c] <= prev else table[c] - prev * 2
        prev = table[c]
    return sum

# OR

def from_roman(num):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,c in enumerate(num):
        print(i,c)
        if (i+1) == len(num) or roman_numerals[c] >= roman_numerals[num[i+1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result
print(from_roman("DDMII"))
# OR
    
val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def main():
    string = str(input('Enter a roman numeral: '))
    string = string.upper()
    total = 0
    while string:
        if len(string) == 1 or val[string[0]] >= val[string[1]]:
            total += val[string[0]]
            string = string[1:]
        else:
            total += val[string[1]] - val[string[0]]
            string = string[2:]
    print (total)

main()


# Solution 1: (Approx Runtime = 52ms)

def romanToInt(self, s: str) -> int:

     roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
     num = 0

     for i in range(len(s)):

        if i!= len(s)-1 and roman[s[i]] < roman[s[i+1]]:
             num += roman[s[i]]*-1
        else:
             num += roman[s[i]]

        return num
     
# Solution 2: (Approx Runtime = 60ms)

def romanToInt(self, s: str) -> int:

     roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
     num = 0

     s = s.replace("IV", "IIII").replace("IX", "VIIII")
     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

     for x in s:
        num += roman[x]
     return num

# Solution 3: (Approx Runtime = 48ms)

def romanToInt(self, s: str) -> int:

     roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
     num = 0

     for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            num += roman[s[i]]*-1
            continue

        num += roman[s[i]]
        num +=roman[s[-1]]
        return num

if __name__ == "__main__":
    roman_string = input("Enter roman figure \n").upper()
    print(roman_to_int(roman_string))
    


