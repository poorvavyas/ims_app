# def highestValuePalindrome(s, n, k):
#     # Write your code here
#     s = list(s)
#     print(s)
#     if len(s) % 2 == 0:
#         # s1 = 0
#         e1 = n // 2 - 1
#         s2 = n // 2
#         # e1 = n-1
#         while e1 >= 0 and s2 < n:
#             if s[e1] != s[s2]:
#                 if s[e1] < s[s2]:
#                     s[e1] = s[s2]
#                 else:
#                     s[s2] = s[e1]
#             k -= 1
#             e1 -= 1
#             s2 += 1
#             print('k : ', k, 'e1 : ', e1, 's2 : ', s2)
#         if k !=0 and k%2 == 0:
#             s1 = 0
#             e2 = n-1
#
#     else:
#         pass
#     print(s)
#
# highestValuePalindrome('291283', 6, 5)

# palindrome using k changes
def maximumPalinUsingKChanges(strr, k):
    palin = strr[::]

    # Initialize l and r by leftmost and
    # rightmost ends
    l = 0
    r = len(strr) - 1

    # first try to make palindrome
    while (l <= r):

        # Replace left and right character by
        # maximum of both
        if (strr[l] != strr[r]):
            palin[l] = palin[r] = max(strr[l], strr[r])

        # print(strr[l],strr[r])
        k -= 1
        l += 1
        r -= 1


    # If k is negative then we can't make
    # palindrome
    if (k < 0):
        return "Not possible"

    l = 0
    r = len(strr) - 1

    while (l <= r):

        # At mid character, if K>0 then change
        # it to 9
        if (l == r):
            if (k > 0):
                palin[l] = '9'

        # If character at lth (same as rth) is
        # less than 9
        if (palin[l] < '9'):

            # If none of them is changed in the
            # previous loop then subtract 2 from K
            # and convert both to 9
            if (k >= 2 and palin[l] == strr[l] and palin[r] == strr[r]):
                k -= 2
                palin[l] = palin[r] = '9'

            # If one of them is changed in the previous
            # loop then subtract 1 from K (1 more is
            # subtracted already) and make them 9
            elif (k >= 1 and (palin[l] != strr[l] or palin[r] != strr[r])):
                k -= 1
                palin[l] = palin[r] = '9'

        l += 1
        r -= 1

    return palin

st = "291283"
strr = [i for i in st]
k = 3
a = maximumPalinUsingKChanges(strr, k)
print("".join(a))
k = 4
a = maximumPalinUsingKChanges(strr, k)
print("".join(a))