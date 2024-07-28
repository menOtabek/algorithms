"""
Nollarni orqaga surish

Berilgan sonlar ro'yxatidagi nollarni ro'yxat orqasiga o'tkazing, lekin boshqa elementlar ketma-ketligi buzilmasin.

Imkon qadar kamroq amal bajaring.

Qo'shimcha xotiradan foydalanmang - amallarni ro'yxat ustida bajaring.
Misol 1:

Kiritish: nums = [0,1,0,3,12]

Natija: [1, 3, 12, 0, 0]

Misol 1:

Kiritish: nums = [0]

Natija: [0]
"""


def move_zeroes(nums: list) -> list:
    count = 0

    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            continue
        nums[i], nums[i - count] = nums[i - count], nums[i]
    return nums


a = move_zeroes([1, 3, 0, 12, 0, 0])
print(a)
