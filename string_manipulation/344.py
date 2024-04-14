def reverseString1(self, s: List[str]) -> None:
    for i in range(len(s)//2):
        temp = s[len(s)-1-i]
        s[len(s) - 1 - i] = s[i]
        s[i] = temp


# use 2 pointer
def reverseString2(self, s: List[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# pythonic
def reverseString3(self, s: List[str]) -> None:
    s.reverse()