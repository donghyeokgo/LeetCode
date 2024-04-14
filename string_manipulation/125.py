import collections


def valid_palindrome0(self, s : str) -> bool:
    str = []

    for char in s:
        if char.isalnum():
            str.append(char.lower())

    if str == []:
        return True

    for i in range(len(str)):
        if str[i] == str[len(str) - 1 - i]:
            if i == len(str) -1:
                return True
        else:
            return False

def valid_palindrome1(self, s : str) -> bool:
    for char in s:
        if char.isalnum():
            str.append(char.lower())

    while str(len) > 1:
        if str.pop(0) != str.pop():
            return False

    return True

def valid_palindrome2(self, s : str) -> bool:
    str: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            str.append(char.lower())

    while len(str) > 1:
        if str.popleft() != str.pop():
            return False
    return True

