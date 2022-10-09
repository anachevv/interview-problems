'''
Examples:
list = ['a', 'b', 'c', 'd', 'e', 'f']

rotate(list, 0)
# ['a', 'b', 'c', 'd', 'e', 'f']

rotate(list, 1)
# ['f', 'a', 'b', 'c', 'd', 'e']

rotate(list, 3)
# ['d', 'e', 'f', 'a', 'b', 'c']
'''


# rotate list
# no time/space requirements
# return "rotated" version of input list


def rotate(my_list, num_rotations):
    part_to_rotate = my_list[-num_rotations::]
    del my_list[-num_rotations::]

    for index in range(len(part_to_rotate)):
        my_list.insert(index, part_to_rotate[index])

    return my_list


#   ### TESTS SHOULD ALL BE TRUE ####
print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd',
                                                                                            'e']))

print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c',
                                                                                            'd']))

print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b',
                                                                                            'c']))

print(
    "{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['c', 'd', 'e', 'f', 'a', 'b'],
                                              rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a',
                                                                                            'b']))
