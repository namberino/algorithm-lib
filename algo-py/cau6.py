# câu 6:
def isBalanced(equation):
    roundBracketCount = 0
    squareBracketCount = 0
    curlyBracketCount = 0

    for letter in equation:
        if letter == '(' or letter == ')':
            roundBracketCount += 1
        if letter == '{' or letter == '}':
            curlyBracketCount += 1
        if letter == '[' or letter == ']':
            squareBracketCount += 1
    
    if roundBracketCount % 2 != 0:
        print("Equation is missing a round bracket")
    if curlyBracketCount % 2 != 0:
        print("Equation is missing a curly bracket")
    if squareBracketCount % 2 != 0:
        print("Equation is missing a square bracket")
    if roundBracketCount % 2 == 0 and curlyBracketCount % 2 == 0 and squareBracketCount % 2 == 0:
        print("Equation is error free")

isBalanced("(2x)^2 + ({9")
