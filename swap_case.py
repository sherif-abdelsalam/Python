def swap_case(s):
    return s.swapcase()

def swap_case_man(s):
    result =  []
    for char in s:
        if(char.isalpha()):
            if char.islower():
                result.append(char.upper())
            elif char.isupper():
                result.append(char.lower())
        else:
            result.append(char)
            
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    