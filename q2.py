def ab(arr):
    """
    Given a string containing only A and B, remove all the consecutive A's and B's.
    :param arr: list
    :return: string
    """
    counter, i = 0, 1
    while i < len(arr):
        if (arr[i-1] == 'A' and arr[i] == 'A') or (arr[i-1] == 'B' and arr[i] == 'B'):
            counter += 1
            arr.pop(i)
            i -= 1
        i += 1
    print('output: ', ''.join(arr), '\nminimum number of required deletions is ', counter) 



if __name__ == '__main__':
    string = 'ABABABA'
    arr = list(string)
    ab(arr)