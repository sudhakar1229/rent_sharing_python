rent=int(input("enter rent"))
current_bill=float(input("enter current bill"))
room_charges=int(input("enter room charges"))
food_bill=int(input("enter food"))
electric_bill=int(input("enter electric"))

total_electricity=current_bill*electric_bill
total_amount=(
    rent+food_bill+room_charges
)

print(total_amount)

