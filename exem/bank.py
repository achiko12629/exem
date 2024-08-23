# Bank System:

# 1.create account
# 2.Deposit
# 3.Withdraw
# 4.Exit


print ("hello to tbc bank .")
name = input("enter your name here")
last_name = input("enter your last name here")
print (f"hello {name} {last_name}")
age = input("enter your age here")
if  age < 18:
  print("your to young")
elif age > 18:
  print("ok")
else:
  print("something went wrong")
password = input(" enter a password that you want to have for your account")

money = input("how much money do you want to deposit in your account?")
print(f"you have {money} dollars in your account")

withdraw = input("how much money do you want to withdraw?")
if withdraw > money :
  print("you dont have enoth money")
elif withdraw < money:
  print("ok,your money id withdrown")
elif withdraw == money:
  print("ok, your money is withdrown")
else :
  print("somthing went wrong")

idk = int(money) - int(withdraw)
print(f"you have {idk} dolars left on your bank account")

print("thanks for using the bank of tbc and have a great day.")



