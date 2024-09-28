i =  1
while i <= 5:
    print(i , "0")
    i+=1
a = 0
for y in range(1,101):
    a += y
print(a)
o = 0
p = 0
for t in range(1,101):
    if t%2==0:
        o+=t
print(o)
an = int(input("take a number"))
for t in range(1,101):
    if t%2!=0:
        p+=t
print(p)
an = int(input("take a number"))
while True:
    print("hi answer the wath we asking and get money")

    print("wath are moth of summer???")
    print("A. October")
    print("B. November")
    print("C. July")
    bank = 0
    ans1 = input("answer - ")

    if ans1 == "C" or ans1 == "c":
        print('your answer is right good job')
        bank += 100
        print("your's bank is", str (bank))

    else:
        print("i am sorry but you are not right")
        print("game over")
        print("you won: ", str(bank))
        break