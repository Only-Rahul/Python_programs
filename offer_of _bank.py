# # create a program to provide the offers to the reggular customer of the bank
# annual_dealing_cash=int(input("Enter the amount ="))
# # making conditions of offer
# if annual_dealing_cash >= 300000:
#     interest_rate = 0.05
# elif annual_dealing_cash >= 600000:
#     interest_rate = 0.09
# elif annual_dealing_cash >= 900000:
#     interest_rate = 0.16
# elif annual_dealing_cash >= 1500000:
#     interest_rate = 0.20
# elif annual_dealing_cash >= 2500000:
#     interest_rate = 0.25
# if interest_rate > 0:
# # calculating the interest
#     print("offer",annual_dealing_cash*interest_rate+annual_dealing_cash)
# else:
#     print("not any offer applied")

annual_dealing_cash = int(input("Enter the amount = "))
interest_rate = 0.00  # Initialize interest_rate
if annual_dealing_cash >= 2500000:
     interest_rate = 0.25
elif annual_dealing_cash >= 1500000:
     interest_rate = 0.20
elif annual_dealing_cash >= 900000:
     interest_rate = 0.16
elif annual_dealing_cash >= 600000:
     interest_rate = 0.09
elif annual_dealing_cash >= 300000:
     interest_rate = 0.05
if interest_rate > 0: 
# Check if an offer was applied
    print("Offer:", annual_dealing_cash * interest_rate + annual_dealing_cash)
else:
    print("Not any offer applied")