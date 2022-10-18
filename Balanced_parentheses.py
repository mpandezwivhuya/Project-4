#Challenge 4
#Balanced parentheses

def Parentheses_balanced(expression):
    s = []
    
    for char in expression:
        if char in ["(", "{", "["]:
            s.append(char)
        else:
            if not s:
                return False
            current_char = s.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if s:
        return False
    else:
        return True

expression =input("Please enter the parentheses: ")

Parentheses_balanced(expression)
            