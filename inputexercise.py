number = int(input("Please enter a 3 digit number: "))
v1 = number // 100 #v1 = 2
v2 = number % 100 #v2 = 35
v3 = v2//10 #v3 = 3
v4 = v2%10  #v4 = 5
print(v4,v3,v1,sep = "")
print(v4 + v3 + v1)