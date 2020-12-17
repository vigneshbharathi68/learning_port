num in range(1,100)

for nums in num:
    if nums % 5==0:
        print(nums)
        break
else:
    print("not found")