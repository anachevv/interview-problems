'''
Description:
You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher.
The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

Example:
abcd xyz
If the shift value, n, is 4, then the encrypted text would be the following: efgh bcd
'''


def encrypt(msg, shift):
    alpha = [chr(x) for x in range(97, 122 + 1)]
    result = []

    for char in msg:
        if char == ' ':
            result.append(char)
        else:
            if alpha.index(char) + shift <= len(alpha):
                result.append(alpha[alpha.index(char) + shift])
            else:
                result.append(alpha[(alpha.index(char) + shift) - len(alpha)])

    result = ''.join(result)

    return result


print(
    encrypt(
        "abcd xyz", 4
    )
)

print(
    encrypt(
        "wayj jzh", 7
    )
)
