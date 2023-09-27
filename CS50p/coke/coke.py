#coke vending machine lab

def main():
    #amount for coke
    a = 50
    #while amount more than 0 do this:
    while a >0:
        #print only when there amount is more than 0.
        if a >0:
            print("Amount Due: ", a)
        #coin insert and coin check for int 5 10 25
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            a -= coin
            #change owed is -ve, therefore use abs(int) to convert
            if a < 0:
                print ("Change owed: ", abs(a))
            #if no balance, close the book.
            elif a == 0:
                print("Change owed: 0")

main()


######## below rest my 5hours. RIP
    # while amount >0:

        # coin = input("Insert Coin: ")
        # amount = amount - int(coin)
        # if amount > 0:
        #     print ("Amount Due: ", amount)
        # elif amount < 0:
        #     print ("Change owed: ", abs(amount))
        # else:
        #     print("Change owed: 0")

# def machine(a):
#     while a >0:
#         print("Amount Due: ", a)
#         coin = input("Insert Coin: ")
#         if coin in [25, 10, 5]:
#             a -= int(coin)
#             if a > 0:
#                 print ("Amount Due: ", a)
#             elif a < 0:
#                 print ("Change owed: ", abs(a))
#             else:
#                 print("Change owed: 0")

# main()

#coke price 50 cents
#machine accepts only 25 10 and 5 cents



# def main():
#     amount_due=50
#     # if amount_due ==50:
#     print("Amount Due: ", amount_due)
#     insert_coin = (input("Insert Coin: "))
#     amount_left = int(amount_due) - int(insert_coin)
#     while amount_left > 0:
#         print("Amount Due: ", amount_left)
#         main()
#     else:
#         print("Change Owed: 0")

# # def ad(n):
# #     n = 50

# # def ic(coin):
# #     coin = (input("Insert Coin: "))
# #     if coin == 5:
# #         return 5
# #     elif coin == 10:
# #         return 10
# #     elif coin == 25:
# #         return 25
# #     else:
# #         return 0



# # def amount_due(ad):

# #     return ad

# def insert_coin(ic):
#     while True:


#         return ic

# # for i in range(amount_due != 0):
# #     if insert_coin != (5, 10, 25):
# #     print("Amount Due: ", amount_due)
# #         elif insert_coin == 5:
# #             print("Amount Due: ", amount_due - insert_coin)



# main()



