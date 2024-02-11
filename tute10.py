# if - elif -else 
applePrice = 200
budget = int(input('Enter Your Budget: '))

if(budget - applePrice >= 500):
    print("Buy 1 kg Apples")
elif(budget - applePrice >= 200):
    print("Buy 1/2 kg Apples")
else:
    print("Don't buy apple")