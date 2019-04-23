def positive_sum(nums):
    return sum([n for n in nums if n>0])


# b=positive_sum([1, 2, 3, 6, 3, 2])
# a=positive_sum([1,2,3,6,-3,2])
# print(a)


def addstf (s):
    res=[c*index for index,c in enumerate(s,start=1)]
    return  '-'.join(map(lambda x:x.capitalize(),res))

print(addstf('sdfdas'))