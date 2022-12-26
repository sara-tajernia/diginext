def string_length(arr, length):
    """
    Given an infinite string s = 'aba' and an integer n, print the number 
    of a's in the first n letters of the infinite string.
    :param arr: list
    :param length: int
    :return: string"""
    out = []
    count , a = 0, 0
    if length == 0:
        return ''
    else:
        while len(out) < length:
            out.append(arr[count%len(arr)])
            if arr[count%len(arr)] == 'a':
                a += 1
            count += 1
    print('output: ', ''.join(out), '\nnumber of a: ', a)

if __name__ == '__main__':
    string = 'aba'
    length = 10
    arr = list(string)
    string_length(arr, length)
    

