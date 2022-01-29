user_input = input("Enter your credit number:")


def checkingNumberlength(user_input):
    if (len(user_input)) == 16:
        print("All is good")
    else:
        print("nothing is good")


checkingNumberlength(user_input)

user_split = [int(x) for x in str(user_input)]

print(user_split)
print(type(user_split))

user_multiply = [c * 2 for c in user_split]
print(user_multiply)


i = 0
even_sum = 0
odd_sum = 0

def luckalgorith(user_multiply):
    while i < len(user_multiply):
        if i % 2 == 0:
            even_sum = even_sum + user_multiply[i]
        else:
            if user_multiply[i] > 9:
                user_multiply[i] = user_multiply[i] - 9
                odd_sum = odd_sum + user_multiply[i]
            else:
                odd_sum = odd_sum + user_multiply[i]
    return even_sum+odd_sum



answer = luckalgorith(user_multiply)

if answer==100:
    print("This credit card number works")
else:
    print("This credit card number doesnt work")



print(answer)
print(even_sum)
print(odd_sum)
