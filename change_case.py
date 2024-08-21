def change_case(s, style):
    result = []
    toggle = False
    
    if style == 'u':
        toggle = s[0].islower()

    for c in s:
        if 'a' <= c <= 'z': 
            if style == 'c':  
                result.append(chr(ord(c) - 32))
            elif style == 's': 
                result.append(c)
            elif style == 'r': 
                result.append(chr(ord(c) - 32))
            elif style == 'u': 
                if toggle:
                    result.append(chr(ord(c) - 32))
                else:
                    result.append(c)
                toggle = not toggle
        elif 'A' <= c <= 'Z': 
            if style == 'c':  
                result.append(c)
            elif style == 's':  
                result.append(chr(ord(c) + 32))
            elif style == 'r': 
                result.append(chr(ord(c) + 32))
            elif style == 'u': 
                if toggle:
                    result.append(chr(ord(c) + 32))
                else:
                    result.append(c)
                toggle = not toggle
        else:
            result.append(c)  

    return ''.join(result)

print(change_case("Om Ingle", "c")) 
print(change_case("Om Ingle", "s"))  
print(change_case("Om Ingle", "r")) 
print(change_case("Om Ingle", "u"))  
print(change_case("om ingle", "u")) 

