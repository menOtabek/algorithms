"""
Ro'yxatni aylantiring

Berilgan ro'yxatni k qadam o'ng tomonga aylantiring.

    Ro'yxatni 1 qadam o'ng tomonga aylantirish, o'ng tomondagi ohirgi elementni, chap tomonning boshiga olib qo'yish degani.

Amalni berilgan ro'yhat ustida bajaring - yangi ro'yxat yaratmang.
Misol 1:

Kiritish: nums = [1,2,3,4,5,6,7], k = 3

Natija: [5,6,7,1,2,3,4]

Tushuntirish:

1-qadam: [7,1,2,3,4,5,6]

2-qadam: [6,7,1,2,3,4,5]

3-qadam: [5,6,7,1,2,3,4]

Misol 2:

Kiritish: nums = [-1,-100,3,99], k = 2

Natija: [3,99,-1,-100]

Tushuntirish:

1-qadam: [99,-1,-100,3]

2-qadam: [3,99,-1,-100]
"""


def reverse_(lst: list, i, j) -> list:
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


def rotate(nums: list, k: int) -> list:
    if k > len(nums):
        k = k % len(nums)
    reverse_(nums, 0, len(nums) - 1)
    reverse_(nums, 0, k - 1)
    reverse_(nums, k, len(nums) - 1)
    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
