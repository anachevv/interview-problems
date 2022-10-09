'''
Examples:
list = ['a', 'b', 'c', 'd', 'e', 'f']

rotate(list, 1)
# ['b', 'c', 'd', 'e', 'f', 'a']

rotate(list, 4)
# ['e', 'f', 'a', 'b', 'c', 'd']
'''


# rotate list
# Constant space requirement
# return input list "rotated"


def rotate(my_list, num_rotations):
    for index in range(len(my_list)):
        if index < num_rotations:
            my_list.append(my_list.pop(0))

    return my_list


#   ### TESTS SHOULD ALL BE TRUE ####
print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['b', 'c', 'd', 'e', 'f', 'a'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['b', 'c', 'd', 'e', 'f',
                                                                                            'a']))

print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['c', 'd', 'e', 'f', 'a', 'b'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['c', 'd', 'e', 'f', 'a',
                                                                                            'b']))

print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b',
                                                                                            'c']))

print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['e', 'f', 'a', 'b', 'c', 'd'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['e', 'f', 'a', 'b', 'c',
                                                                                            'd']))
