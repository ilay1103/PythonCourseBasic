num = int(input("Enter three digits: "))
sum = int(num/100) + int(num / 10 % 10) + num % 10
avg = int(sum / 3)
rest= sum % 3
print(sum)
print(avg)
print(rest)
print(not(rest))