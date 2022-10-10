def encrypt(msg, shift):
    alpha = [chr(x) for x in range(97, 122 + 1)]
    msg_lst = [x for x in msg]
    result = []

    for char in msg_lst:
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
