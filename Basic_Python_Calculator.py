first_num=int(input("Enter first number: "))
sec_num=int(input("Enter second number: "))
operation=input('''ENTER AN OPERATION:
    +,-,*,/: ''')
if operation=="+":
    print(first_num+sec_num)
elif operation=="-":
    print(first_num-sec_num)
elif operation=="*":
    print(first_num*sec_num)
elif operation=="/":
    print(first_num/sec_num)
else:
    print("Error404-_-")
