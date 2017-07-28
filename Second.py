'''
for x in range(10,40,5):

    print (x)
    while x <=30:
        print("true")
        #x += 5
        x = x + 5
        print("Current number is " , x)
'''

'''
for x in range(1,101):
    if x % 4 == 0:
        print(x)
        if x == 44:
            print (x)
            break
'''

numberList = [2,4,6,8,10]

totalNumber = len(numberList)
print(len(numberList))

for n in range(1,totalNumber + 1):
    if n in numberList:
        print(n)
        continue

    #print(n)

#assigns default value if no arguments is provided
def myFirstPythodMethod(inputParameters = "abc"):
    totalValue = inputParameters + 1
    return totalValue

print(myFirstPythodMethod(2))


#Simple Calculator
def simpleAdditionMethodThatTakesInUnlimitedArguments(*randomName):
    totalAmount = 0
    print(randomName)
    for i in randomName:
        print(i)
        totalAmount += i
    print(totalAmount)


simpleAdditionMethodThatTakesInUnlimitedArguments(33,333,33,33)