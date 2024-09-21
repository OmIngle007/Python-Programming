def check_validity(text: str) -> str:
    bracket_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    open_brackets = set(bracket_pairs.values())
    close_brackets = set(bracket_pairs.keys())

    stack = []
    
    for char in text:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return "Invalid: closing bracket without matching opening bracket"
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return "Invalid: mismatched closing bracket"
        elif not char.isalnum() and char not in "+-*/":
            return "Invalid: contains invalid characters"

    if stack:
        return "Invalid: imbalanced brackets (unmatched opening brackets)"
    
    return "Valid"


def get_valid_invalid_text_count(texts):
    valid_count = 0
    invalid_count = 0
    
    for item in texts:
        if isinstance(item, str):
            result = check_validity(item)
            if result == "Valid":
                valid_count += 1
            else:
                invalid_count += 1
        else:
            continue
    
    return valid_count, invalid_count


texts = ['[{(', [45], '()']
valid_count, invalid_count = get_valid_invalid_text_count(texts)
print(f"({valid_count},{invalid_count})")

