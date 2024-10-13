# შექმენით set'ი და გამოიყენეთ ყველა
#  თვისება თუ ფუნქცია რაც შეიძლება set'ებთან
#  გამოვიყენოთ 


nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

nums.update([17, 18])
nums.remove(1)
nums.add(2)
nums.discard(3)
nums.discard(10)

sigdze = len(nums)

nums2 = {5, 62,"bmw", "iphone", 8, 9}

print(nums)
print("სიგრძე:", sigdze)

nums.clear()
print(nums)