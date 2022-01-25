from stack import Stack

def validate_brackets(string):
    valid = {"]":"[", "}":"{", ")":"("}
    stack = Stack()
    for char in string:
        if char in valid.values():
            stack.push(char)
        elif char in valid.keys():
            if valid[char] == stack.peek():
                stack.pop()
    
    return stack.is_empty()