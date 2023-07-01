# i = 0
# for x in [1,2,3, 3]:
#     if x == 3:
#         i = i + 1
# print(i)


# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.
def array_front9(nums, nums1):
  i=0
  count = 0
  for x in range(len(nums)-1):
    res1 = (nums[i:i+2])
    print(res1 + ">")
    y=0
    for x in range(len(nums1) - 1):
      print(nums1[y:y + 2])
      if res1 == (nums1[y:y + 2]):

        count = count + 1
      y = y + 1
    print("***")
    i = i+1
  print(count)

array_front9("xxcaazz", "xxbaaz")
