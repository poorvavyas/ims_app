x = [2, 7, 13, 5, 9, 4, 1]

b = float('inf')
s = x[-1]
max_p = 0
bi = 0
si = len(x)-1
for i in range(len(x)-2, -1, -1):
    if x[i] > s:
        s = x[i]
        si = i
    else:
        if x[i] < b:
            b = x[i]
            bi = i
    if bi<si:
        max_p = max(max_p, s-b)
print(max_p)


# class Source:
#     pass
# # getallsources
#
# class destination:
#     pass
# # getall destination

class bus:
    pass
# get source and destination according to bus

class Payment:
    pass

class booking:
    pass
# method ticketbooking with bus sorce destination detail
# calling payment class for making payment once confirmation is received confirm booking msg

