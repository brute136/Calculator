print("\033[1;32;40m Welcome Try and give me feedback please")

num = input("Enter Your First Number\n")
num2 = input("Enter Your Second Number\n")
print("Attention Use Number Not symblus")
print("1.+")
print("2.-")
print("3./")
print("4.*")
nums3 = input("Choose Numer\n:-")

if nums3 == "1":
	print(int(num) + int(num2))
elif nums3 == "2":
    print(int(num) - int(num2))
elif nums3 == "3":
    print(int(num) / int(num2))
elif nums3 == "4":
    print(int(num) * int(nums2))
 
