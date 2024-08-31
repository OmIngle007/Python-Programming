def DFA(text):

    state = "start"
    

    for char in text:
        if state == "start":
            if char == 'a':
                state = "ends_with_a"
            elif char == 'b':
                state = "not_ends_with_a"
        elif state == "ends_with_a":
            if char == 'a':
                state = "ends_with_a"
            elif char == 'b':
                state = "not_ends_with_a"
        elif state == "not_ends_with_a":
            if char == 'a':
                state = "ends_with_a"
            elif char == 'b':
                state = "not_ends_with_a"


    if state == "ends_with_a":
        return "accepted"
    else:
        return "rejected"


print(DFA("abba")) 
print(DFA("abab"))

