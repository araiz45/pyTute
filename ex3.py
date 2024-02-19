ques = [
    ["How many color present in the flag of Pakistan", "2", 100],
    ["How many province did Pakistan have?", "4", 200],
    ["How many computer do you have on your home", "2", 2200]
]

amount = 0
for subques in ques:
    print(subques[0])
    answer = input("Enter your Ans: ").lower()
    subques[1].lower()
    if(answer == subques[1]):
        print("Correct")
        amount = amount + subques[2] 
        print("Amount Won: RS", amount)
    else:
        print("Wrong")
        print("Amount Won: RS",amount)
        break